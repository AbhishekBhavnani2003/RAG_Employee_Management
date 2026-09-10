from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from conf.config import CHUNK_SIZE, CHUNK_OVERLAPPING


def load_document(file_path):
    extension = file_path.strip().split(".")[-1]
    match extension:
        case "pdf":
            loader = PyPDFLoader(file_path=file_path)
            return loader
        case "docx":
            loader = Docx2txtLoader(file_path=file_path)
            return loader
        case _:
            print(f"Unsupported File Extension : {extension}")
            return None


def get_document(file_path):
    loader = load_document(file_path=file_path)
    if loader:
        document_text = loader.load()
        return document_text
    return None


def get_chunks(document):

    spliter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAPPING
    )

    chunks = spliter.split_documents(documents=document)
    return chunks
