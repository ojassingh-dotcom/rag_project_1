from models.retriever import Maximum_Marginal_Relevance_vector_retriever
from models.llm_summerization import llm_summarization 

def query_controller(query):
    """Controller function to handle the query and retrieve relevant documents."""
    print("\n running query controller \n")
    relevant_docs = Maximum_Marginal_Relevance_vector_retriever(query)
    return llm_summarization(query, relevant_docs)