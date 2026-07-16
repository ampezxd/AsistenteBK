from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from my_keys import PINECONE_API_KEY

hf_emb_model = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-small"
)

vector_store = PineconeVectorStore(
    embedding=hf_emb_model,
    host="https://asistente-bk-sqql9qx.svc.aped-4627-b74a.pinecone.io",
    pinecone_api_key=PINECONE_API_KEY
)

retriever = vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k":8,
        "fetch_k":25
    }
)