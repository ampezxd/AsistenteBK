from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_huggingface import HuggingFaceEmbeddings
from procesamiento import hf_fragmentos
from my_keys import PINECONE_API_KEY

hf_emb_model = HuggingFaceEmbeddings(model_name ='intfloat/multilingual-e5-small')
pc = Pinecone(api_key=PINECONE_API_KEY)
Index = pc.Index('asistente-bk')
vector_store = PineconeVectorStore(
    embedding=hf_emb_model,
    host='https://asistente-bk-sqql9qx.svc.aped-4627-b74a.pinecone.io',
    pinecone_api_key=PINECONE_API_KEY
)

vector_store.add_documents(hf_fragmentos)