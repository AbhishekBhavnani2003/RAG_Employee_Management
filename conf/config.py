from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
VECTOR_DB = os.getenv("VECTOR_DB")
VECTOR_DB_URL = os.getenv("VECTOR_DB_URL")
OLLAMA_URL = os.getenv("OLLAMA_URL")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
INDEX_NAME = os.getenv("INDEX_NAME")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))
CHUNK_OVERLAPPING = int(os.getenv("CHUNK_OVERLAPPING"))
FILE_NAME = os.getenv("FILE_NAME")
