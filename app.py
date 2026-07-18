import streamlit as st
from rag import responder

st.set_page_config(
    page_title="Bienvenido al asistende BK",
    page_icon="🍔",
    layout="centered"
)

st.title("🍔 Asistente BK")
st.caption(
    "Consulta el Reglamento Interno de Burger King Colombia mediante IA y RAG."
)

st.divider()

if "chat" not in st.session_state:
    st.session_state.chat = []

pregunta = st.chat_input(
    "Haz una pregunta sobre el reglamento"
)

if pregunta:

    with st.chat_message("user"):
        st.markdown(pregunta)

    with st.spinner("Consultando el reglamento..."):
        resultado = responder(pregunta)

    st.session_state.chat.append(resultado | {"pregunta": pregunta})


for mensaje in reversed(st.session_state.chat):

    with st.chat_message("user"):
        st.markdown(mensaje["pregunta"])

    with st.chat_message("assistant"):

        st.markdown(mensaje["respuesta"])

        #if mensaje.get("fuentes"):
#
 #           st.caption("📚 Fuente consultada")
#
 #           for fuente in mensaje["fuentes"]:
  #              st.write(f"• {fuente}")

   #     if mensaje.get("documentos"):

    #        with st.expander("Ver fragmentos recuperados"):

     #           for doc in mensaje["documentos"]:

      #              st.code(doc.page_content)
                