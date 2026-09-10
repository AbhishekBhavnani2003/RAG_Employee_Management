from fastapi import FastAPI
from rag.retrieval import get_answer

app = FastAPI()


@app.get("/")
def temp_function():
    return "Server is running"


@app.post("/send-message")
def send_message(user_message: str):
    result = get_answer(user_query=user_message)
    print(result)
    return result
