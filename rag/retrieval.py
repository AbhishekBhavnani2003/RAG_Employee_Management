from langchain_qdrant import QdrantVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", api_key=GEMINI_API_KEY)

embedding_model = OllamaEmbeddings(
    model="embeddinggemma:300m", base_url="localhost:11434"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="localhost:6333",
    embedding=embedding_model,
    collection_name="employee-management",
)


query = "List 5 faqs regarding leaves"

result = vector_db.similarity_search(query=query, k=4)

print(result)
print("----------------------------")
print(len(result))

print("=" * 60)


for i in result:
    print("=" * 60)
    print(i.page_content)


SYSTEM_PROMPT = f""" 
You are the knowledge base ai asistant which gives answer based on the available context . 

CONTEXT: 
{result}

RULE: 
Strictly Answer based on the avaialble content , If you not find answer then reply with - Sorry , Given document does not contain information. 
"""


answer = llm.invoke([SystemMessage(content=SYSTEM_PROMPT), HumanMessage(content=query)])

print("=" * 60)
print(f"Answer : {answer.content[0]["text"]}")
