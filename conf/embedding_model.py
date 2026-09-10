from langchain_ollama import OllamaEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from conf.config import GEMINI_API_KEY, OLLAMA_URL

ollama_embedding_model = OllamaEmbeddings(
    model="embeddinggemma:300m", base_url=OLLAMA_URL
)

gemini_embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2", api_key=GEMINI_API_KEY
)
