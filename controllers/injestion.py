from models.document_loader import load_documents
from models.chunker import chunk_documents
from models.vector_store import create_vector_store
from models.document_loader import merge_pages_by_source


def run_ingestion(docs_path="docs", persist_directory="dnb/chroma_db"):
    """orchestrates the full ingestion pipeline: load -> chunk -> embed & store"""

    documents = load_documents(docs_path)
    print(f"\nBefore merge: {len(documents)} documents\n")
    single_documents = merge_pages_by_source(documents)
    print(f"\nAfter merge: {len(single_documents)} documents\n")
    chunks = chunk_documents(single_documents, docs_path)
    vectorstore = create_vector_store(chunks, persist_directory)

    return {
        "document_count": len(single_documents),
        "chunk_count": len(chunks),
        "vectorstore": vectorstore
    }

# if __name__ == "__main__":
#     print("Running ingestion pipeline...")
#     result = run_ingestion(docs_path="docs", persist_directory="dnb/chroma_db")
#     print(f"Documents loaded: {result['document_count']}")
#     print(f"Chunks created: {result['chunk_count']}")
    
