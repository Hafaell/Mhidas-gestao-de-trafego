#!/usr/bin/env python3
"""Números do perfil do Instagram num período, já divididos em janelas de até 30 dias (limite da API).

Uso:
    python3 relatorio/instagram_perfil.py <ig-user-id> <início AAAA-MM-DD> <fim AAAA-MM-DD>

O fim é incluído (01 a 31/10 = mês inteiro). Imprime um JSON:
    visitas_perfil_total  profile_views (orgânico + anúncio)
    cliques_bio_total     website_clicks (orgânico + anúncio)
    alcance               soma do reach de cada dia (é o "Alcance" do relatório feito à mão)
    novos_seguidores      follows_and_unfollows / FOLLOWER (seguidores novos do perfil)
    alcance_unico         reach sem repetir pessoa (aproximado se o período passar de 30 dias)
    janelas, alcance_unico_aproximado

Saída: 0 = ok | 2 = token vencido ou inválido (erro 190) | 1 = outro erro. Nunca mostra o token.
"""
import json
import sys

from midas.instagram_perfil import ErroInstagram, PerfilInstagram, como_dict


def main() -> None:
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    ig, inicio, fim = sys.argv[1:]
    try:
        numeros = PerfilInstagram(ig).numeros(inicio, fim)
    except ErroInstagram as erro:
        sys.stderr.write(f"ERRO da API do Instagram: {erro} (código {erro.codigo})\n")
        sys.exit(2 if erro.codigo == 190 else 1)
    print(json.dumps(como_dict(numeros), ensure_ascii=False))


if __name__ == "__main__":
    main()
