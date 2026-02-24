from langchain_chroma import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

PERSIST_DIR = "chroma_db"

def ingest_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    # splits = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    vectordb = Chroma(
        collection_name="docs",
        embedding_function=embeddings,
        persist_directory=PERSIST_DIR
    )

    vectordb.add_documents(documents)
    return vectordb

def get_retriever():
    embeddings = OpenAIEmbeddings()

    vectordb = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embeddings
    )

    return vectordb.as_retriever(search_kwargs={"k": 3})