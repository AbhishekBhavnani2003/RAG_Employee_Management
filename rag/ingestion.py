from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore

from langchain_pinecone import PineconeVectorStore

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

file_path = "data/employeemng.pdf"

loader = PyPDFLoader(file_path=file_path)
document_text = loader.load()

# print(document_text)

spliter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

chunks = spliter.split_documents(documents=document_text)

# print(chunks)

print("---------------------------------------")

print(len(chunks))

embedding_model = OllamaEmbeddings(
    model="embeddinggemma:300m", base_url="localhost:11434"
)

# embedding_gemini_model = GoogleGenerativeAIEmbeddings(
#     model="gemini-embedding-2", api_key=GEMINI_API_KEY
# )


# vector_db = QdrantVectorStore.from_documents(
#     url="localhost:6333",
#     documents=chunks,
#     embedding=embedding_model,
#     collection_name="employee-management",
# )

# vector_db = QdrantVectorStore.from_documents(
#     url="localhost:6333",
#     documents=chunks,
#     embedding=embedding_gemini_model,
#     collection_name="employee-management-gemini",
# )
vector_db = PineconeVectorStore.from_documents(
    pinecone_api_key=PINECONE_API_KEY,
    index_name="ragsession",
    documents=chunks,
    embedding=embedding_model,
    namespace="employee-management",
)
