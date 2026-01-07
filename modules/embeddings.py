from langchain.embeddings import HuggingFaceEmbeddings

def load_embeddings():
    """
    Download and return the HuggingFace embeddings Model
    """
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    embeddings=HuggingFaceEmbeddings(
        model_name=model_name,
    )
    return embeddings
