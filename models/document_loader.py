import os
from xml.dom.minidom import Document
# from pdf2image import convert_from_path
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_core.documents import Document

def load_documents(docs_path="docs"):
    """load all PDF files from the docs directory"""
    print(f"Loading documents from {docs_path}...")

    if not os.path.exists(docs_path):
        raise FileNotFoundError(f"the directory {docs_path} does not exist. Please create it and add your files")

    loader = DirectoryLoader(
        path=docs_path,
        glob="*.pdf",
        loader_cls=PyPDFLoader,
    )
    documents = loader.load()

    if len(documents) == 0:
        raise FileNotFoundError(f"No .pdf files found in {docs_path}. Please add your PDF documents")

    return documents


def merge_pages_by_source(documents):
    """combine per-page Documents into one Document per source file"""
    merged = {}
    for doc in documents:
        source = doc.metadata["source"]
        if source not in merged:
            merged[source] = doc.page_content
        else:
            merged[source] += "\n" + doc.page_content
    return [Document(page_content=text, metadata={"source": source}) for source, text in merged.items()]