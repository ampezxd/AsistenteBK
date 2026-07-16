from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError
from retriever import retriever
from llm import llm


def responder(pregunta: str):

    docs = retriever.invoke(pregunta)
    print("\n" + "="*80)
    print("DOCUMENTOS RECUPERADOS")
    print("="*80)

    """for i, doc in enumerate(docs):
        print(f"\n--- Chunk {i+1} ---")
        print(doc.page_content[:1000])

    print("="*80 + "\n")"""""

    contexto = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
Eres un asistente experto en el Reglamento Interno de Trabajo de Burger King Colombia.

Utiliza exclusivamente la información proporcionada.

No copies el texto literalmente.

Redacta una respuesta natural, clara y profesional.

Si el contexto no contiene la respuesta responde exactamente:

"No encontré esa información en el reglamento."

Si el contexto sí contiene la respuesta, explica el contenido con tus propias palabras.

Contexto:
{contexto}

Pregunta:
{pregunta}

Respuesta:
"""

    try:
        respuesta = llm.invoke(prompt)
        return {
            "respuesta": respuesta.content,
            "fuentes": docs
        }

    except ChatGoogleGenerativeAIError:
        return (
            "⚠️ Se alcanzó el límite de la API de Gemini. "
            "Espera un momento e inténtalo nuevamente."
    )