from langchain_huggingface import HuggingFaceEmbeddings

from langchain_chroma import Chroma

persistent_directory= "dnb/chroma_db"

#load embeddings and vector store
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
    )
db = Chroma(
    persist_directory=persistent_directory,
    embedding_function=embedding_model,
    collection_metadata={"hnsw:space":"cosine"}

)
# query="How does the suggest() function keep response times bounded even for very common prefixes?"
def Maximum_Marginal_Relevance_vector_retriever(query):
        
    

    
    # ──────────────────────────────────────────────────────────────────
    #  Maximum Marginal Relevance (MMR)
    # Balances relevance and diversity - avoids redundant results
    # ──────────────────────────────────────────────────────────────────

    print("\n===  Maximum Marginal Relevance (MMR) ===")
    retriever = db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 5,           # Final number of docs
            "fetch_k": 15,    # Initial pool to select from
            "lambda_mult": 0.5  # 0=max diversity, 1=max relevance
        }
    )
        
  
    


    relevant_docs = retriever.invoke(query)
    print(f"Retrieved {len(relevant_docs)} documents (λ=0.5):\n")
    print(type(relevant_docs))

    print(f"user query{query}")
    #display context
    print("--- Context ---")
    for i ,doc in enumerate(relevant_docs,1):
        print(f"Document{i}:\n{doc.page_content}\n") 

    print ("-----------------___meta data of the retrieved documents___-------------")
    for i, doc in enumerate(relevant_docs,1):
        print(f"Document {i} metadata:\n{doc.metadata}\n")
    return relevant_docs

