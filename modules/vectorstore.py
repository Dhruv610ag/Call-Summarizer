from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
from modules.embeddings import load_embeddings
from modules.dataloading import split_extracted_text, text_extractor
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.getenv("Pinecone_API_Key")
pc = Pinecone(api_key=PINECONE_API_KEY)


def make_index(pc, index_name="Convox-Ai"):
    """
    Creates or loads a Pinecone index.
    """
    if not pc.has_index(index_name):
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
    return pc.Index(index_name)


def delete_index(pc, index_name):
    """
    Deletes a Pinecone index.
    """
    if pc.has_index(index_name):
        pc.delete_index(index_name)


def insert_data_into_vectorstore(pc, audio_file_path, index_name="Convox-Ai"):
    """
    Transcribes audio, chunks text, embeds and stores in Pinecone.
    """
    transcript = text_extractor(audio_file_path)
    chunks = split_extracted_text(transcript)
    embeddings = load_embeddings()
    make_index(pc, index_name)
    vectorstore = PineconeVectorStore.from_texts(
        texts=chunks,
        embedding=embeddings,
        index_name=index_name
    )
    return vectorstore


def create_retriever(pc, audio_file_path, index_name="Convox-Ai"):
    """
    Creates a retriever from Pinecone vector store.
    """
    vectorstore = insert_data_into_vectorstore(
        pc=pc,
        audio_file_path=audio_file_path,
        index_name=index_name
    )
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
