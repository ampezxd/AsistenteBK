from langchain_core. tools import BaseTool
from pydantic import Field
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from my_keys import GEMINI_API_KEY
from my_models import GEMINI_FLASH


class HerramientaAnalisis42Horas(BaseTool):
    name: str = "analizar_42_horas"

    description: str = Field (
        "Analiza el reglamento de la reducción de 42 horas laborales y responde preguntas relacionadas con como se implementara este nuevo reglamento y sobre que habla"
    )

    return_direct: bool = False

    def _run(self, pregunta: str) -> str:
        print ("Herramienta 42 horas fue llamada.")

        ruta = Path ("knowledge_base/ley_42_horas.txt")

        contenido = ruta.read_text(encoding="utf-8")

        llm = ChatGoogleGenerativeAI(
            model = GEMINI_FLASH,
            api_key=GEMINI_API_KEY
        )