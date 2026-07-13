from langchain_core.tools import BaseTool
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from my_keys import GEMINI_API_KEY
from my_models import GEMINI_FLASH
from pypdf import PdfReader

class HerramientaAnalisisReglamento(BaseTool):
    name: str = "analizar_reglamento"

    description: str = "Analiza el reglamento de la empresa y responde preguntas relacionadas con horarios, descansos, permisos y contratos."

    return_direct: bool = False

    def _run(self, pregunta: str) -> str:
        print ("Herramienta analisis de reglamento Bk fue llamada.")

        reader = PdfReader("knowledge_base/ReglamentoBKCOL2026.pdf")

        contenido = ""

        for pagina in reader.pages:
            texto = pagina.extract_text()

        if texto:
            contenido += texto + "\n"

        llm = ChatGoogleGenerativeAI(
            model=GEMINI_FLASH,
            api_key=GEMINI_API_KEY
        )