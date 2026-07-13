from langchain_core. tools import BaseTool
from pydantic import Field
from pathlib import Path
from langchain_google_genai import ChatGoogleGenerativeAI
from my_keys import GEMINI_API_KEY
from my_models import GEMINI_FLASH


class HerramientaAnalisis42Horas(BaseTool):
    name: str = "analizar_42_horas"

    description: str = Field (
        "Lee exclusivamente la Ley 2101 de reducción de jornada laboral."
    )

    return_direct: bool = False

    def _run(self, pregunta: str) -> str:
        print ("Herramienta 42 horas fue llamada.")

        ruta = Path ("knowledge_base/ley_42_horas.txt")

        contenido = ruta.read_text(encoding="utf-8")

        print("\n === CONTENIDO DEVUELTO POR LA HERRAMIENTA ===")
        print (contenido[:1000])
        print("==============================================\n")

        return contenido