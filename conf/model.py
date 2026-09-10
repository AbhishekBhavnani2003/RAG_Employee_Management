from langchain_google_genai import ChatGoogleGenerativeAI
from conf.config import GEMINI_API_KEY

llm_model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite", api_key=GEMINI_API_KEY
)
