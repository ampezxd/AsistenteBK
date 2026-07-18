from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
#from my_keys import GEMINI_API_KEY
#from my_models import GEMINI_FLASH
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
GEMINI_FLASH = st.secrets["GEMINI_FLASH"]

llm = ChatGoogleGenerativeAI(
    model=GEMINI_FLASH,
    google_api_key=GEMINI_API_KEY,
    temperature=0
)