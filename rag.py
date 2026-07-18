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
Responde de forma clara y profesional.

Reglas:

- No copies literalmente el documento.
- Resume la información.
- Utiliza títulos.
- Utiliza listas con viñetas cuando sea posible.
- Resalta en negrita los conceptos importantes.
- Si la información proviene del reglamento, indícalo al final.
- Si la respuesta no está en el reglamento, dilo claramente.
- No agregues información inventada.

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