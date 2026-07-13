from langchain_core.tools import BaseTool
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from my_keys import GEMINI_API_KEY
from my_models import GEMINI_FLASH
from pypdf import PdfReader

class HerramientaAnalisisReglamento(BaseTool):
    name: str = "analizar_reglamento"

    description: str = "Lee exclusivamente el reglamento interno de Burger King."

    return_direct: bool = False

    def _run(self, pregunta: str) -> str:
        print("Herramienta analisis de reglamento Bk fue llamada.")

        ruta = Path("knowledge_base/reglamentoBkcol.txt")

        contenido = ruta.read_text(encoding="utf-8")

        print("\n=== CONTENIDO DEVUELTO POR LA HERRAMIENTA ===")
        print(contenido[:1000])
        print("===========================================\n")

        return contenido