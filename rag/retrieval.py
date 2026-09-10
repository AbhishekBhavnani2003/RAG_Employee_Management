from langchain_core.messages import HumanMessage, SystemMessage
from conf.vector_db import read_data
from conf.system_prompt import get_system_prompt
from conf.model import llm_model


def get_answer(user_query: str):
    vector_store = read_data()
    if vector_store:
        context = vector_store.similarity_search(query=user_query, k=5)
        system_prompt = get_system_prompt(context=context)
        answer = llm_model.invoke(
            [SystemMessage(content=system_prompt), HumanMessage(content=user_query)]
        )
        print(answer)
        return answer.content[0]["text"]
    else:
        return f"Error Proceesing Query : {user_query}"
