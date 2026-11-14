#!/usr/bin/env python3
"""Gera o relatório Meta Ads de um cliente (HTML + PDF) a partir de um JSON de dados.

Uso:
    python3 relatorio/gerar.py relatorio/exemplos/cliente-exemplo.json
    python3 relatorio/gerar.py dados.json --saida saida/ --sem-pdf

O JSON segue o formato de relatorio/exemplos/cliente-exemplo.json.
Seções ausentes no JSON simplesmente não aparecem no relatório.
"""
from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import re
import subprocess
import sys
import unicodedata
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent

# Ordem fixa das seções no relatório (topo -> meio -> fundo).
ORDEM_SECOES = ["instagram", "video", "whatsapp"]

ETAPAS = {
    "instagram": {"etapa": "topo", "nome_etapa": "Topo", "rotulo": "Pessoas novas"},
    "video": {"etapa": "meio", "nome_etapa": "Meio", "rotulo": "Vídeo"},
    "whatsapp": {"etapa": "fundo", "nome_etapa": "Fundo", "rotulo": "Foco em consulta"},
}

MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]


# ---------- formatação pt-BR ----------

def _milhar(txt: str) -> str:
    return txt.replace(",", "X").replace(".", ",").replace("X", ".")


def fmt_int(v) -> str:
    if v is None:
        return "–"
    return _milhar(f"{round(v):,}")


def fmt_brl(v) -> str:
    if v is None:
        return "–"
    return "R$ " + _milhar(f"{v:,.2f}")


def fmt_pct(v, casas: int = 1) -> str:
    if v is None:
        return "–"
    return _milhar(f"{v * 100:,.{casas}f}") + "%"


def fmt_data(iso: str) -> str:
    d = date.fromisoformat(iso)
    return d.strftime("%d/%m/%Y")


def fmt_data_curta(iso: str) -> str:
    d = date.fromisoformat(iso)
    return f"{d.day:02d} {MESES[d.month - 1]}"


def div(a, b):
    if a is None or b in (None, 0):
        return None
    return a / b


# ---------- métricas ----------

def variacao(atual, anterior, menor_melhor: bool = False):
    """Retorna dict com a variação vs período anterior, ou None se não houver base."""
    if atual is None or anterior in (None, 0):
        return None
    pct = (atual - anterior) / anterior
    if abs(pct) < 0.005:
        estado = "neutro"
    else:
        melhorou = pct < 0 if menor_melhor else pct > 0
        estado = "bom" if melhorou else "ruim"
    seta = "▲" if pct > 0 else ("▼" if pct < 0 else "•")
    return {"texto": f"{seta} {fmt_pct(abs(pct))}", "estado": estado}


def kpi(rotulo, valor, fmt, anterior=None, menor_melhor=False, nota=None, destaque=False):
    return {
        "rotulo": rotulo,
        "valor": fmt(valor),
        "var": variacao(valor, anterior, menor_melhor),
        "nota": nota,
        "destaque": destaque,
    }


def montar_instagram(d):
    a = d.get("anterior", {})
    custo_seg = div(d["investido"], d["novos_seguidores"])
    custo_seg_ant = div(a.get("investido"), a.get("novos_seguidores"))
    kpis = [
        kpi("Valor investido", d["investido"], fmt_brl, a.get("investido"), menor_melhor=None),
        kpi("Alcance", d["alcance"], fmt_int, a.get("alcance")),
        kpi("Visitas ao perfil", d["visitas_perfil"], fmt_int, a.get("visitas_perfil")),
        kpi("Cliques na bio", d["cliques_bio"], fmt_int, a.get("cliques_bio")),
        kpi("Novos seguidores", d["novos_seguidores"], fmt_int, a.get("novos_seguidores"), destaque=True),
        kpi("Custo por seguidor", custo_seg, fmt_brl, custo_seg_ant, menor_melhor=True, destaque=True),
    ]
    passos = [
        {"rotulo": "Alcance", "valor": fmt_int(d["alcance"])},
        {"rotulo": "Visitas ao perfil", "valor": fmt_int(d["visitas_perfil"]),
         "taxa": fmt_pct(div(d["visitas_perfil"], d["alcance"])), "taxa_txt": "visitaram o perfil"},
        {"rotulo": "Novos seguidores", "valor": fmt_int(d["novos_seguidores"]),
         "taxa": fmt_pct(div(d["novos_seguidores"], d["visitas_perfil"])), "taxa_txt": "das visitas viraram seguidores"},
    ]
    return {
        "titulo": "Crescimento do Instagram",
        "icone": "instagram",
        "kpis": kpis,
        "fluxo": {"titulo": "Do alcance ao seguidor", "passos": passos},
        "destaque": {"rotulo": "Novos seguidores", "valor": fmt_int(d["novos_seguidores"]),
                     "nota": f"{fmt_brl(custo_seg)} por seguidor"},
    }


def montar_video(d):
    a = d.get("anterior", {})
    inv, inv_a = d["investido"], a.get("investido")

    # Linha de cima: gasto, visualização de 15 seg e custo (como no modelo do gestor).
    topo = [
        kpi("Valor gasto", inv, fmt_brl, inv_a, menor_melhor=None),
        kpi("Visualização 15 seg", d["views_15s"], fmt_int, a.get("views_15s"), destaque=True),
        kpi("Custo 15 seg", div(inv, d["views_15s"]), fmt_brl,
            div(inv_a, a.get("views_15s")), menor_melhor=True, destaque=True),
    ]
    # Tempo médio assistido (opcional): entra como 4º card da linha de cima.
    if d.get("tempo_medio_s") is not None:
        topo.append(kpi("Tempo médio assistido", d["tempo_medio_s"], lambda v: f"{round(v)} s",
                        a.get("tempo_medio_s")))
    # Três linhas de pares: quantidade de views no ponto do vídeo + valor gasto / views.
    pares = []
    for chave, rotulo in [("video_50", "Vídeo 50%"), ("video_75", "Vídeo 75%"), ("video_95", "Vídeo 95%")]:
        pares.append({
            "qtd": kpi(rotulo, d[chave], fmt_int, a.get(chave)),
            "custo": kpi(f"Valor gasto / {rotulo}", div(inv, d[chave]), fmt_brl,
                         div(inv_a, a.get(chave)), menor_melhor=True),
        })

    # Funil à direita: 15 seg -> 50% -> 95%. A largura é fixa e sempre diminui
    # (é um desenho de funil, não uma escala), os números reais ficam escritos dentro.
    etapas_funil = [("Vídeo 15 seg", d["views_15s"], 200, 158),
                    ("Vídeo 50%", d["video_50"], 150, 108),
                    ("Vídeo 95%", d["video_95"], 100, 50)]
    cores = ["#de6a35", "#c0521f", "#96401a"]
    altura, folga, funil = 64, 6, []
    for i, (rotulo, valor, larg_topo, larg_base) in enumerate(etapas_funil):
        y0 = i * (altura + folga)
        y1 = y0 + altura
        pts = (f"{100 - larg_topo / 2:g},{y0} {100 + larg_topo / 2:g},{y0} "
               f"{100 + larg_base / 2:g},{y1} {100 - larg_base / 2:g},{y1}")
        funil.append({"rotulo": rotulo, "valor": fmt_int(valor), "pontos": pts,
                      "cor": cores[i], "y_rot": y0 + altura / 2 - 9, "y_val": y0 + altura / 2 + 14})
    return {
        "titulo": "Visualização de vídeo",
        "tema": d.get("tema"),
        "icone": "video",
        "kpis": None,
        "vv": {"topo": topo, "pares": pares,
               "funil": {"titulo": "Funil de visualização", "etapas": funil,
                         "altura_total": 3 * altura + 2 * folga,
                         "retencao_final": fmt_pct(div(d["video_95"], d["views_15s"]))}},
        "destaque": {"rotulo": "Visualizações de 15 seg", "valor": fmt_int(d["views_15s"]),
                     "nota": f"{fmt_brl(div(d['investido'], d['views_15s']))} por visualização"},
    }


def montar_whatsapp(d):
    a = d.get("anterior", {})
    custo_conv = div(d["investido"], d["conversas"])
    custo_conv_ant = div(a.get("investido"), a.get("conversas"))
    kpis = [
        kpi("Valor investido", d["investido"], fmt_brl, a.get("investido"), menor_melhor=None),
        kpi("Impressões", d["impressoes"], fmt_int, a.get("impressoes")),
        kpi("Alcance", d["alcance"], fmt_int, a.get("alcance")),
        kpi("Cliques", d["cliques"], fmt_int, a.get("cliques")),
        kpi("Conversas iniciadas", d["conversas"], fmt_int, a.get("conversas"), destaque=True),
        kpi("Custo por conversa", custo_conv, fmt_brl, custo_conv_ant, menor_melhor=True, destaque=True),
    ]
    passos = [
        {"rotulo": "Impressões", "valor": fmt_int(d["impressoes"])},
        {"rotulo": "Cliques", "valor": fmt_int(d["cliques"]),
         "taxa": fmt_pct(div(d["cliques"], d["impressoes"]), 2), "taxa_txt": "clicaram no anúncio"},
        {"rotulo": "Conversas iniciadas", "valor": fmt_int(d["conversas"]),
         "taxa": fmt_pct(div(d["conversas"], d["cliques"])), "taxa_txt": "dos cliques viraram conversa"},
    ]
    return {
        "titulo": "Captação de leads no WhatsApp",
        "icone": "whatsapp",
        "kpis": kpis,
        "fluxo": {"titulo": "Do anúncio à conversa", "passos": passos},
        "destaque": {"rotulo": "Conversas iniciadas", "valor": fmt_int(d["conversas"]),
                     "nota": f"{fmt_brl(custo_conv)} por conversa"},
    }


MONTADORES = {"instagram": montar_instagram, "video": montar_video, "whatsapp": montar_whatsapp}


def iniciais(nome: str) -> str:
    partes = [p for p in re.split(r"\s+", nome) if p and not p.lower().rstrip(".") in {"dr", "dra"}]
    return "".join(p[0] for p in partes[:2]).upper() or "?"


def foto_data_uri(caminho: str | None, base: Path) -> str | None:
    if not caminho:
        return None
    if caminho.startswith(("http://", "https://", "data:")):
        return caminho
    p = (base / caminho).resolve()
    if not p.exists():
        return None
    mime = mimetypes.guess_type(p.name)[0] or "image/jpeg"
    return f"data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"


def slug(txt: str) -> str:
    txt = unicodedata.normalize("NFKD", txt).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", txt.lower()).strip("-")


def montar_contexto(dados: dict, base: Path) -> dict:
    secoes_in = dados.get("secoes", {})
    secoes = []
    for chave in ORDEM_SECOES:
        if chave in secoes_in and secoes_in[chave]:
            s = MONTADORES[chave](secoes_in[chave])
            s.update(ETAPAS[chave])
            s["chave"] = chave
            s["investido"] = secoes_in[chave]["investido"]
            s["investido_ant"] = secoes_in[chave].get("anterior", {}).get("investido")
            s["comentario"] = secoes_in[chave].get("comentario")
            secoes.append(s)

    total = sum(s["investido"] for s in secoes)
    total_ant_partes = [s["investido_ant"] for s in secoes]
    total_ant = sum(total_ant_partes) if all(v is not None for v in total_ant_partes) else None
    for s in secoes:
        s["investido_fmt"] = fmt_brl(s["investido"])
        s["share"] = div(s["investido"], total) or 0
        s["share_fmt"] = fmt_pct(s["share"], 0)

    cliente = dados["cliente"]
    periodo = dados["periodo"]
    ant = dados.get("periodo_anterior")
    return {
        "agencia": dados.get("agencia", "Agência Lupa"),
        "cliente": cliente,
        "iniciais": iniciais(cliente["nome"]),
        "foto": foto_data_uri(cliente.get("foto"), base),
        "periodo_txt": f"{fmt_data(periodo['inicio'])} a {fmt_data(periodo['fim'])}",
        "anterior_txt": (f"{fmt_data_curta(ant['inicio'])} a {fmt_data_curta(ant['fim'])}" if ant else None),
        "total_fmt": fmt_brl(total),
        "total_var": variacao(total, total_ant, menor_melhor=None),
        "secoes": secoes,
        "observacoes": dados.get("observacoes"),
        "comparacao": montar_comparacao(secoes_in, total, total_ant) if ant else [],
        "gerado_em": date.today().strftime("%d/%m/%Y"),
        "total_paginas": 1 + len(secoes),
    }


def montar_comparacao(sec, total, total_ant):
    """Linhas da tabela 'este período x período anterior' da página 1."""
    linhas = [{"rotulo": "Investimento total", "etapa": None, "atual": fmt_brl(total),
               "anterior": fmt_brl(total_ant), "var": variacao(total, total_ant), "neutro": True}]

    def add(chave, rotulo, f, campo=None, custo_de=None, menor_melhor=False):
        d = sec.get(chave)
        if not d:
            return
        a = d.get("anterior", {})
        if custo_de:
            atual, ant = div(d["investido"], d[custo_de]), div(a.get("investido"), a.get(custo_de))
        else:
            atual, ant = d[campo], a.get(campo)
        linhas.append({"rotulo": rotulo, "etapa": ETAPAS[chave]["etapa"], "atual": f(atual),
                       "anterior": f(ant), "var": variacao(atual, ant, menor_melhor)})

    add("instagram", "Novos seguidores", fmt_int, "novos_seguidores")
    add("instagram", "Custo por seguidor", fmt_brl, custo_de="novos_seguidores", menor_melhor=True)
    add("video", "Visualizações de 15 seg", fmt_int, "views_15s")
    add("video", "Custo por visualização de 15 seg", fmt_brl, custo_de="views_15s", menor_melhor=True)
    add("whatsapp", "Conversas iniciadas", fmt_int, "conversas")
    add("whatsapp", "Custo por conversa", fmt_brl, custo_de="conversas", menor_melhor=True)
    return linhas


def variacao_neutra(ctx):
    # Investimento não é "bom" nem "ruim": mostra a variação em cinza.
    def limpar(v):
        if v:
            v["estado"] = "neutro"
    limpar(ctx["total_var"])
    for c in ctx["comparacao"]:
        if c.get("neutro"):
            limpar(c["var"])
    for s in ctx["secoes"]:
        cards = list(s["kpis"] or [])
        if s.get("vv"):
            cards += s["vv"]["topo"]
        for k in cards:
            # "Valor gasto / Vídeo X" é custo (cair é bom), não investimento: não mexer.
            if k["rotulo"].startswith("Valor") and "/" not in k["rotulo"]:
                limpar(k["var"])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dados", help="arquivo JSON com os dados do cliente")
    ap.add_argument("--saida", default=str(RAIZ / "saida"), help="pasta de saída (padrão: saida/)")
    ap.add_argument("--sem-pdf", action="store_true", help="gera só o HTML")
    args = ap.parse_args()

    arq = Path(args.dados).resolve()
    dados = json.loads(arq.read_text(encoding="utf-8"))
    ctx = montar_contexto(dados, arq.parent)
    variacao_neutra(ctx)

    env = Environment(loader=FileSystemLoader(AQUI / "modelo"), autoescape=select_autoescape(["html", "j2"]))
    html = env.get_template("relatorio.html.j2").render(**ctx)

    saida = Path(args.saida)
    saida.mkdir(parents=True, exist_ok=True)
    nome = f"relatorio-{slug(dados['cliente']['nome'])}-{dados['periodo']['inicio'][:7]}"
    html_path = saida / f"{nome}.html"
    html_path.write_text(html, encoding="utf-8")
    print(f"HTML: {html_path}")

    if not args.sem_pdf:
        pdf_path = saida / f"{nome}.pdf"
        subprocess.run(["node", str(AQUI / "pdf.js"), str(html_path), str(pdf_path)], check=True)
        print(f"PDF:  {pdf_path}")


if __name__ == "__main__":
    sys.exit(main())
