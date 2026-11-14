#!/usr/bin/env python3
"""Servidor local para ver o relatório no navegador e baixar o PDF.

Uso:
    python3 relatorio/servir.py                      # usa o relatório mais recente de saida/
    python3 relatorio/servir.py nome-do-relatorio    # sem extensão
    python3 relatorio/servir.py --porta 8080

Abre em http://localhost:8000 (só acessível neste computador).
"""
import argparse
import html
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "saida"

PAGINA = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title>
<style>
  :root {{ --fundo:#e9ecf2; --barra:#0b1020; --texto:#fff; --botao:#1baf7a; --botao-hover:#159868; }}
  * {{ box-sizing: border-box; }}
  html, body {{ height: 100%; margin: 0; }}
  body {{ display: flex; flex-direction: column; background: var(--fundo); font-family: Arial, Helvetica, sans-serif; }}
  header {{ background: var(--barra); color: var(--texto); padding: 12px 24px; display: flex;
           align-items: center; justify-content: space-between; gap: 16px; flex-wrap: wrap; }}
  header strong {{ font-size: 15px; letter-spacing: .02em; }}
  header span {{ font-size: 12px; opacity: .7; display: block; margin-top: 2px; }}
  .acoes {{ display: flex; gap: 10px; }}
  a.btn {{ background: var(--botao); color: #fff; text-decoration: none; font-weight: 700; font-size: 14px;
          padding: 10px 18px; border-radius: 8px; }}
  a.btn:hover {{ background: var(--botao-hover); }}
  a.btn.sec {{ background: transparent; border: 1px solid rgba(255,255,255,.4); }}
  a.btn.sec:hover {{ background: rgba(255,255,255,.1); }}
  main {{ flex: 1; display: flex; justify-content: center; padding: 16px; min-height: 0; }}
  iframe {{ width: 100%; max-width: 860px; height: 100%; border: 0; background: #fff;
           border-radius: 8px; box-shadow: 0 2px 12px rgba(0,0,0,.15); }}
</style>
</head>
<body>
<header>
  <div><strong>{titulo}</strong><span>Agência Lupa · visualização local</span></div>
  <div class="acoes">
    <a class="btn sec" href="/relatorio.html" target="_blank" rel="noopener">Abrir em nova aba</a>
    <a class="btn" href="/baixar" download="{nome_pdf}">Baixar PDF</a>
  </div>
</header>
<main><iframe src="/relatorio.html" title="Relatório"></iframe></main>
</body>
</html>
"""


def escolher_relatorio(nome):
    if nome:
        base = SAIDA / nome
        if not base.with_suffix(".html").exists():
            sys.exit(f"Não achei {base.with_suffix('.html')}. Gere o relatório antes com relatorio/gerar.py.")
        return base
    htmls = sorted(SAIDA.glob("*.html"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not htmls:
        sys.exit("Nenhum relatório em saida/. Gere um antes com relatorio/gerar.py.")
    return htmls[0].with_suffix("")


def fazer_handler(base: Path):
    html_path = base.with_suffix(".html")
    pdf_path = base.with_suffix(".pdf")
    titulo = base.name.replace("relatorio-", "Relatório ").replace("-", " ")

    class Handler(BaseHTTPRequestHandler):
        def _enviar(self, status, tipo, corpo, extra=None):
            self.send_response(status)
            self.send_header("Content-Type", tipo)
            self.send_header("Content-Length", str(len(corpo)))
            self.send_header("Cache-Control", "no-store")
            for k, v in (extra or {}).items():
                self.send_header(k, v)
            self.end_headers()
            self.wfile.write(corpo)

        def do_GET(self):
            rota = self.path.split("?")[0]
            if rota in ("/", "/index.html"):
                pagina = PAGINA.format(titulo=html.escape(titulo), nome_pdf=html.escape(pdf_path.name))
                self._enviar(200, "text/html; charset=utf-8", pagina.encode("utf-8"))
            elif rota == "/relatorio.html":
                self._enviar(200, "text/html; charset=utf-8", html_path.read_bytes())
            elif rota == "/baixar":
                if not pdf_path.exists():
                    self._enviar(404, "text/plain; charset=utf-8", "PDF não encontrado. Gere com relatorio/gerar.py.".encode("utf-8"))
                    return
                self._enviar(200, "application/pdf", pdf_path.read_bytes(),
                             {"Content-Disposition": f'attachment; filename="{pdf_path.name}"'})
            else:
                self._enviar(404, "text/plain; charset=utf-8", b"Nao encontrado")

        def log_message(self, fmt, *args):
            sys.stderr.write("[servir] " + (fmt % args) + "\n")

    return Handler


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("nome", nargs="?", help="nome do relatório em saida/, sem extensão (padrão: o mais recente)")
    ap.add_argument("--porta", type=int, default=8000)
    ap.add_argument("--sem-abrir", action="store_true", help="não abre o navegador")
    args = ap.parse_args()

    base = escolher_relatorio(args.nome)
    # 127.0.0.1: só este computador acessa
    servidor = ThreadingHTTPServer(("127.0.0.1", args.porta), fazer_handler(base))
    url = f"http://localhost:{args.porta}"
    print(f"Relatório: {base.name}\nAcesse: {url}\nCtrl+C para parar.")
    if not args.sem_abrir:
        webbrowser.open(url)
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor parado.")


if __name__ == "__main__":
    main()
