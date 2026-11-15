"""Seções do relatório. Para criar uma seção nova: uma classe em um arquivo novo e uma linha aqui."""
from .base import Fluxo, LinhaComparacao, PassoFluxo, Secao
from .instagram import SecaoInstagram, SecaoInstagramOrganico
from .landing_page import SecaoLandingPage
from .video import SecaoVideo, SecaoVideoTopo
from .whatsapp import SecaoWhatsapp

# Ordem fixa no relatório: topo -> meio -> fundo.
SECOES_NA_ORDEM = [SecaoInstagram, SecaoInstagramOrganico, SecaoVideoTopo, SecaoVideo,
                   SecaoLandingPage, SecaoWhatsapp]

__all__ = ["Secao", "Fluxo", "PassoFluxo", "LinhaComparacao",
           "SecaoInstagram", "SecaoInstagramOrganico", "SecaoVideoTopo", "SecaoVideo",
           "SecaoLandingPage", "SecaoWhatsapp", "SECOES_NA_ORDEM"]
