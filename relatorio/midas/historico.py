"""Histórico mensal de um cliente: poucos números por mês, para o gráfico de evolução.

Fica em clientes/historico/<slug-do-cliente>.json (fora do git, dura de um mês para o outro):
    {"2026-10": {"inicio": "2026-10-01", "fim": "2026-10-31", "investido": 3387.45,
                 "novos_seguidores": 561, "views_15s": 8240, "conversas": 141}, ...}
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

from .config import PASTA_HISTORICO


class Historico:
    def __init__(self, slug: str, pasta: Path = PASTA_HISTORICO):
        self.arquivo = pasta / f"{slug}.json"
        self.meses: Dict[str, dict] = self._ler()

    def _ler(self) -> Dict[str, dict]:
        if not self.arquivo.exists():
            return {}
        try:
            return json.loads(self.arquivo.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            sys.exit(f"Histórico ilegível: {self.arquivo}. Corrija ou apague o arquivo e gere de novo.")

    def registrar(self, mes: str, inicio: str, fim: str, valores: dict, sobrescrever: bool = True) -> None:
        """Grava os números de um mês. Com sobrescrever=False, não mexe num mês que já existe."""
        if mes in self.meses and not sobrescrever:
            return
        self.meses[mes] = {"inicio": inicio, "fim": fim, **valores}

    def salvar(self) -> Path:
        self.arquivo.parent.mkdir(parents=True, exist_ok=True)
        ordenado = dict(sorted(self.meses.items()))
        self.arquivo.write_text(json.dumps(ordenado, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        return self.arquivo

    def meses_antes_de(self, mes: str) -> List[Tuple[str, dict]]:
        return [(m, v) for m, v in sorted(self.meses.items()) if m < mes]
