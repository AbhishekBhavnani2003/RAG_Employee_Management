from conf.document_loader import get_document, get_chunks
from conf.vector_db import insert_data


def training(file_path: str):
    document_text_result = get_document(file_path=file_path)
    if document_text_result:
        document_chunks = get_chunks(document_text_result)
        vector_result = insert_data(chunks=document_chunks)
        if vector_result:
            return f" Give file : {file_path} is trained "
        else:
            return f" Error processing Given file : {file_path} "

    else:
        return f" Error processing Given file : {file_path} "
