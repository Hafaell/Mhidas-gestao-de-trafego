"""Formatação no padrão brasileiro: R$ 1.737,03, milhar com ponto, decimal com vírgula."""
import re
import unicodedata
from datetime import date

MESES = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]


class Formatador:
    """Só métodos estáticos: recebe um valor cru e devolve o texto pronto para o relatório."""

    @staticmethod
    def _padrao_br(texto: str) -> str:
        """Troca o padrão americano (1,234.56) pelo brasileiro (1.234,56)."""
        return texto.replace(",", "X").replace(".", ",").replace("X", ".")

    @staticmethod
    def inteiro(valor) -> str:
        if valor is None:
            return "–"
        return Formatador._padrao_br(f"{round(valor):,}")

    @staticmethod
    def moeda(valor) -> str:
        if valor is None:
            return "–"
        return "R$ " + Formatador._padrao_br(f"{valor:,.2f}")

    @staticmethod
    def percentual(valor, casas: int = 1) -> str:
        """`valor` em fração: 0.153 vira "15,3%"."""
        if valor is None:
            return "–"
        return Formatador._padrao_br(f"{valor * 100:,.{casas}f}") + "%"

    @staticmethod
    def data(iso: str) -> str:
        return date.fromisoformat(iso).strftime("%d/%m/%Y")

    @staticmethod
    def data_curta(iso: str) -> str:
        d = date.fromisoformat(iso)
        return f"{d.day:02d} {MESES[d.month - 1]}"

    @staticmethod
    def slug(texto: str) -> str:
        """"Dra. Ana Exemplo" vira "dra-ana-exemplo" (para nome de arquivo)."""
        texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
        return re.sub(r"[^a-z0-9]+", "-", texto.lower()).strip("-")
