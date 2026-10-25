from langchain_huggingface import HuggingFaceEmbeddings
#embedding model
from langchain_chroma import Chroma




def create_vector_store(chunks, persist_directory="dnb/chroma_db"):
    """create and persist chromadb vector store"""
    print("creating embeddings and storing in chromDB...")

    embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
    )
    
    #create ChromaDB vector store
    print("--- Creating vector store---")
    vectorstore= Chroma.from_documents(
        documents= chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
        collection_metadata={"hnsw:space":"cosine"}
    )
    print("--- Finished vector store---")
    print(f"Vector store created and saved to {persist_directory}")
    return vectorstore


# chunks = chunk_documents(docs_path="docs")

# vectorstore = create_vector_store(chunks,persist_directory="dnb/chroma_db")