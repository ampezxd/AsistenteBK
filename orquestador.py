from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from my_models import GEMINI_FLASH
from my_keys import GEMINI_API_KEY
from tools.herramienta_analisis_reglamento import HerramientaAnalisisReglamento
from tools.herramienta_analisis_42_horas import HerramientaAnalisis42Horas

class AgenteOrquestador:

    def __init__(self):

        llm = ChatGoogleGenerativeAI(
            model=GEMINI_FLASH,
            api_key=GEMINI_API_KEY
        )

        self.agente = create_agent(
            model=llm,
            tools=[
                HerramientaAnalisisReglamento(),
                HerramientaAnalisis42Horas()
            ],
            system_prompt= """
                Eres un asistente de inteligencia artificial que ayudara a los trabajadores de Burger King a resolver sus dudas sobre horarios, descansos, permisos y contratos. Tu objetivo es proporcionar respuestas claras y concisas a las preguntas de los empleados, utilizando un lenguaje amigable y profesional.

                No iventes información, si no conoces la respuesta, indica que no tienes información sobre el tema y sugiere al empleado que consulte con su supervisor o con el departamento de recursos humanos.
    """

        )