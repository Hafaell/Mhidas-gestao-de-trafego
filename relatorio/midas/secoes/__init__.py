"""Seções do relatório. Para criar uma seção nova: uma classe em um arquivo novo e uma linha aqui."""
from .base import Fluxo, LinhaComparacao, PassoFluxo, Secao
from .instagram import SecaoInstagram
from .video import SecaoVideo
from .whatsapp import SecaoWhatsapp

# Ordem fixa no relatório: topo -> meio -> fundo.
SECOES_NA_ORDEM = [SecaoInstagram, SecaoVideo, SecaoWhatsapp]

__all__ = ["Secao", "Fluxo", "PassoFluxo", "LinhaComparacao",
           "SecaoInstagram", "SecaoVideo", "SecaoWhatsapp", "SECOES_NA_ORDEM"]
