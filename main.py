from rag.ingestion import training
from rag.retrieval import get_answer

import uvicorn


def main():
    file_path = "/home/scs/Documents/AiSession/employee-management/data/THQSCS0003.pdf"
    # result = training(file_path=file_path)
    # print(result)
    # query = "Give details of gst in invoice"
    # result = get_answer(user_query=query)
    # print(result)
    uvicorn.run("app.server:app", host="0.0.0.0", port=5000, reload=True)


if __name__ == "__main__":
    main()
