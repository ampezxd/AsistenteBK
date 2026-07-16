import streamlit as st
from rag import responder


st.set_page_config(
    page_title="Asistente BK",
    page_icon="🍔",
    layout="centered"
)

st.title("🍔 Asistente BK")
st.subheader("Consulta el Reglamento Interno de Burger King Colombia")

st.write(
    """
    Este asistente utiliza una arquitectura **RAG**
    para responder preguntas únicamente con información
    del Reglamento Interno de Trabajo.
    """
)

st.divider()



if "chat" not in st.session_state:
    st.session_state.chat = []


pregunta = st.text_input(
    "Consulta sobre el reglamento de trabajo",
    placeholder="Ejemplo: ¿Cuánto dura el descanso del personal operativo?"
)


if st.button("Preguntar"):

    if pregunta.strip() == "":
        st.warning("Escribe una pregunta.")
        st.stop()

    with st.spinner("Buscando información en el reglamento..."):

        respuesta = responder(pregunta)

    st.session_state.chat.append(
        {
            "pregunta": pregunta,
            "respuesta": respuesta
        }
    )

#with st.sidebar:

#    st.header("Acerca del proyecto")

#    st.write("""
    #Arquitectura

    #• LangChain
   # • Pinecone
  #  • Gemini
   # • Streamlit
  #  • HuggingFace Embeddings
 #   """)

for mensaje in reversed(st.session_state.chat):

    with st.chat_message("user"):
        st.write(mensaje["pregunta"])

    with st.chat_message("assistant"):
        st.write(mensaje["respuesta"])