from langchain_pinecone import PineconeSparseVectorStore
from pinecone import Pinecone,ServerlessSpec
from modules.embeddings import download_embeddings
from modules.dataloading import split_extracted_text,text_extractor
from dotenv import load_dotenv
import os
load_dotenv()
Pinecone_API_Key=os.environ.get("Pinecone_API_Key")
pc = Pinecone(api_key=Pinecone_API_Key)

def make_index(pc,index_name):
    """
    Creates a Pinecone index with the specified name and configuration.
    """
    index_name="Convox-Ai"
    if not pc.has_index(index_name):
        pc.create_index(
            name = index_name,
            dimension=384,  # Dimension of the embeddings
            metric= "cosine",  # Cosine similarity
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
    index = pc.Index(index_name)
    return index

def delete_index(pc,index_name):
    """
    Deletes a Pinecone index with the specified name.
    """
    if pc.has_index(index_name):
        pc.delete_index(index_name)
        print(f"Index '{index_name}' deleted successfully.")
    else:
        print(f"Index '{index_name}' does not exist.")

def inserting_data_into_vectore(pc,index_name="Convox-Ai"):
    """
    Inserting the data into the vector Store.
    """
    index=make_index(pc,index_name)
    embeddings=download_embeddings()
    docsearch=PineconeSparseVectorStore.from_documents(
        documents=split_extracted_text(text_extractor),
        index_name=index,
        embedding=embeddings
    )
    return docsearch

def create_retriever():
    """
    Creaing the retriever from the vector store.
    """
    docsearch=inserting_data_into_vectore()
    retriever=docsearch.as_retriever(search_type="similarity")
    return retriever