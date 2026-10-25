from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from datetime import datetime

start_time = datetime.now()

print("=" * 50)
print(f"Program Started At: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 50)

persistent_directory = "dnb/chroma_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=persistent_directory,
    embedding_function=embedding_model,
    collection_metadata={"hnsw:space": "cosine"}
)

def llm_summarization(query, relevant_docs):
    combined_input = f"""Based on the following documents, please answer this question: {query}

    Documents:
    {chr(10).join([f"- {doc.page_content}" for doc in relevant_docs])}

    Please provide a clear, helpful answer using only the information from these documents. 
    If you can't find the answer in the documents, say "I don't have enough information to answer
    that question based on the provided documents.
    "
    """

    # The llm model is used to generate the answer based on the context provided by the relevant documents retrieved from the vector store.
    model = ChatOllama(model="llama3")

    messages = [
        SystemMessage(content="You are a helpful assistant , and instead of using using llm stay strictly to the chunks provided in the documents and do not make up any information., and if you dont know the answer you say i dont know"),
        HumanMessage(content=combined_input),
    ]

    result = model.invoke(messages)

    # print(f"\n this is the entire content of the result object: {result} \n")

    print(result.content)