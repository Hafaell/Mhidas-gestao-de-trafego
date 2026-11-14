#!/usr/bin/env python3
"""Confere o token do Instagram antes de gerar relatórios (os cliques na bio dependem dele).

Uso: python3 relatorio/verificar_token.py

Saída: 0 = ok | 1 = vence em menos de 7 dias | 2 = vencido ou inválido | 3 = não deu para verificar.
Só mostra a data de vencimento, nunca o token.
"""
import sys

from midas.token_instagram import TokenInstagram


def main() -> None:
    resultado = TokenInstagram().verificar()
    print(resultado.mensagem)
    sys.exit(resultado.codigo)


if __name__ == "__main__":
    main()
