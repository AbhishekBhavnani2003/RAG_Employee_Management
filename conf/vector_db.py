from langchain_qdrant import QdrantVectorStore
from langchain_pinecone import PineconeVectorStore
from conf.config import (
    VECTOR_DB,
    PINECONE_API_KEY,
    COLLECTION_NAME,
    INDEX_NAME,
    VECTOR_DB_URL,
)
from conf.embedding_model import ollama_embedding_model


def insert_data(chunks):
    match VECTOR_DB:
        case "qdrant":
            QdrantVectorStore.from_documents(
                url=VECTOR_DB_URL,
                documents=chunks,
                embedding=ollama_embedding_model,
                collection_name=COLLECTION_NAME,
            )

            return "Data Inserted"

        case "pinecone":
            PineconeVectorStore.from_documents(
                pinecone_api_key=PINECONE_API_KEY,
                index_name=INDEX_NAME,
                documents=chunks,
                embedding=ollama_embedding_model,
                namespace=COLLECTION_NAME,
            )

            return "Data Inserted"

        case _:
            print("Vector DB not supported")

            return None


def read_data():
    match VECTOR_DB:
        case "qdrant":
            return QdrantVectorStore.from_existing_collection(
                url=VECTOR_DB_URL,
                embedding=ollama_embedding_model,
                collection_name=COLLECTION_NAME,
            )

        case "pinecone":
            return None
            # PineconeVectorStore.from_texts(
            #     pinecone_api_key=PINECONE_API_KEY,
            #     index_name=INDEX_NAME,
            #     embedding=ollama_embedding_model,
            #     namespace=COLLECTION_NAME,
            # )

        case _:

            print("Vector DB not supported")
            return None
