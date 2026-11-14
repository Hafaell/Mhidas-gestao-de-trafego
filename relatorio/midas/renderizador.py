"""Transforma um Relatorio em arquivo HTML usando um modelo (pasta de relatorio/modelos/)."""
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .relatorio import Relatorio


class RenderizadorHtml:
    """Um modelo tem esta forma:
        <modelo>/html/relatorio.html.j2   página principal (usa componentes/ e paginas/)
        <modelo>/css/relatorio.css        estilo, ligado ao HTML por <link>
    """

    def __init__(self, pasta_modelo: Path):
        self.pasta_html = pasta_modelo / "html"
        self.css = pasta_modelo / "css" / "relatorio.css"
        self.ambiente = Environment(loader=FileSystemLoader(self.pasta_html),
                                    autoescape=select_autoescape(["html", "j2"]))

    def renderizar(self, relatorio: Relatorio) -> str:
        return self.ambiente.get_template("relatorio.html.j2").render(relatorio=relatorio)

    def gravar(self, relatorio: Relatorio, pasta_saida: Path) -> Path:
        """Grava <saida>/<nome>.html e copia o relatorio.css para a mesma pasta."""
        pasta_saida.mkdir(parents=True, exist_ok=True)
        destino = pasta_saida / f"{relatorio.nome_arquivo}.html"
        destino.write_text(self.renderizar(relatorio), encoding="utf-8")
        shutil.copyfile(self.css, pasta_saida / self.css.name)
        return destino
