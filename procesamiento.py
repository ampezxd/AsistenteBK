from transformers import AutoTokenizer #AutoModel
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

emb_tokenizer = AutoTokenizer.from_pretrained('intfloat/multilingual-e5-small')
#emb_model = AutoModel.from_pretrained('intfloat/multilingual-e5-small')

#Cargamos el documento
loader = TextLoader(
    "knowledge_base/reglamentoBkcol.txt",
    encoding="utf-8"
)

all_docs = loader.load()



hf_splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
    tokenizer=emb_tokenizer,
    separators=[
        "Artículo",
        "CAPÍTULO",
        "\n\n",
        "\n",
        " ",
        ""
    ],
    chunk_size=480,
    chunk_overlap=50,
)

hf_fragmentos = hf_splitter.split_documents(all_docs)
len(hf_fragmentos)

