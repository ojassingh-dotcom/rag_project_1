from controllers.injestion import run_ingestion
from controllers.query_controller import query_controller


if __name__ == "__main__":
    # Run the ingestion pipeline
    print("Running ingestion pipeline...")
    result = run_ingestion(docs_path="docs", persist_directory="dnb/chroma_db")
    print(f"Documents loaded: {result['document_count']}")
    print(f"Chunks created: {result['chunk_count']}")

    # Example query
    query = "What is the difference between CharacterTextSplitter and RecursiveCharacterTextSplitter?"
    # print("\nRunning query controller...")
    query_controller(query)
  

