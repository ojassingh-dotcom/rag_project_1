from langchain_experimental.text_splitter import SemanticChunker
from langchain_text_splitters import CharacterTextSplitter
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_core.documents import Document
# from langchain_text_splitters import RecursiveCharacterTextSplittersf
def chunk_documents(documents,docs_path="docs"):
    """Load documents and chunk them into semantic chunks"""



    print("\n" + "=" * 60)
    print(" RECURSIVE CHARACTER TEXT SPLITTER SOLUTION")
    print("=" * 60)

    Splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

    docs = Splitter.split_documents(documents)

    print(f"Total chunks created: {len(docs)} \n")
    print("Sample chunk content for document 0: \n")


    print(docs[0].page_content)
    print("\n Sample chunk content for document 1: \n")
    # print(docs[1].page_content)
    # print("Sample chunk metadata for document 1: \n")

    # print(docs[1].page_content)
    return docs

