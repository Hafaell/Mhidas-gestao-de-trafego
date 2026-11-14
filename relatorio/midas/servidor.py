"""Abre um relatório em localhost: a página, o botão "Baixar PDF" e os arquivos do relatório."""
import sys
import tempfile
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .config import PASTA_VISUALIZADOR, SAIDA
from .exportador_pdf import ExportadorPdf


class ServidorLocal:
    """Serve um relatório da pasta de saída (temporária). Só aceita conexão deste computador (127.0.0.1)."""

    def __init__(self, nome: str, exportador: ExportadorPdf, porta: int = 8000, pasta_saida: Path = SAIDA):
        self.pasta_saida = pasta_saida
        self.html = pasta_saida / f"{nome}.html"
        if not self.html.exists():
            sys.exit(f"Não achei {self.html}. Gere o relatório antes com relatorio/gerar.py.")
        self.nome_pdf = f"{nome}.pdf"
        self.titulo = nome.replace("relatorio-", "Relatório ").replace("-", " ")
        self.exportador = exportador
        self.porta = porta
        self.ambiente = Environment(loader=FileSystemLoader(PASTA_VISUALIZADOR),
                                    autoescape=select_autoescape(["html", "j2"]))

    @staticmethod
    def relatorio_mais_recente(pasta_saida: Path = SAIDA) -> str:
        htmls = sorted(pasta_saida.glob("*.html"), key=lambda p: p.stat().st_mtime, reverse=True)
        if not htmls:
            sys.exit(f"Nenhum relatório em {pasta_saida}. Gere um antes com relatorio/gerar.py.")
        return htmls[0].stem

    @property
    def url(self) -> str:
        return f"http://localhost:{self.porta}"

    # ---- conteúdo de cada rota ----

    def pagina_inicial(self) -> bytes:
        return self.ambiente.get_template("visualizador.html.j2").render(
            titulo=self.titulo, nome_pdf=self.nome_pdf).encode("utf-8")

    def gerar_pdf(self) -> Optional[bytes]:
        """O PDF não fica salvo: é gerado na hora, a partir do HTML."""
        with tempfile.TemporaryDirectory() as tmp:
            destino = Path(tmp) / self.nome_pdf
            try:
                self.exportador.exportar(self.html, destino)
            except Exception as erro:  # noqa: BLE001 (qualquer falha vira resposta 500)
                sys.stderr.write(f"{erro}\n")
                return None
            return destino.read_bytes() if destino.exists() else None

    def _rotas(self) -> dict:
        """rota -> (tipo, função que devolve os bytes)."""
        html_utf8 = "text/html; charset=utf-8"
        css_utf8 = "text/css; charset=utf-8"
        return {
            "/": (html_utf8, self.pagina_inicial),
            "/index.html": (html_utf8, self.pagina_inicial),
            "/relatorio.html": (html_utf8, self.html.read_bytes),
            "/relatorio.css": (css_utf8, (self.pasta_saida / "relatorio.css").read_bytes),
            "/visualizador.css": (css_utf8, (PASTA_VISUALIZADOR / "visualizador.css").read_bytes),
        }

    def _criar_handler(self):
        servidor = self

        class Handler(BaseHTTPRequestHandler):
            def _enviar(self, status, tipo, corpo, extra=None):
                self.send_response(status)
                self.send_header("Content-Type", tipo)
                self.send_header("Content-Length", str(len(corpo)))
                self.send_header("Cache-Control", "no-store")
                for chave, valor in (extra or {}).items():
                    self.send_header(chave, valor)
                self.end_headers()
                self.wfile.write(corpo)

            def do_GET(self):
                rota = self.path.split("?")[0]
                if rota == "/baixar":
                    pdf = servidor.gerar_pdf()
                    if pdf is None:
                        self._enviar(500, "text/plain; charset=utf-8", "Não consegui gerar o PDF.".encode("utf-8"))
                    else:
                        self._enviar(200, "application/pdf", pdf,
                                     {"Content-Disposition": f'attachment; filename="{servidor.nome_pdf}"'})
                    return
                try:
                    tipo, ler = servidor._rotas().get(rota, (None, None))
                    if ler is None:
                        self._enviar(404, "text/plain; charset=utf-8", b"Nao encontrado")
                    else:
                        self._enviar(200, tipo, ler())
                except FileNotFoundError:
                    self._enviar(404, "text/plain; charset=utf-8", b"Nao encontrado")

            def log_message(self, fmt, *args):
                sys.stderr.write("[servir] " + (fmt % args) + "\n")

        return Handler

    def iniciar(self, abrir_navegador: bool = True) -> None:
        servidor = ThreadingHTTPServer(("127.0.0.1", self.porta), self._criar_handler())
        print(f"Relatório: {self.html.stem}\nAcesse: {self.url}\nCtrl+C para parar.")
        if abrir_navegador:
            webbrowser.open(self.url)
        try:
            servidor.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor parado.")
