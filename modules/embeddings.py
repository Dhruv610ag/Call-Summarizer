from langchain.embeddings import HuggingFaceEmbeddings

def get_embeddings(model_name: str = "sentence-tranformers/all-MiniLM-L6-v2")->HuggingFaceEmbeddings:
    """
    This function initializes and returns a HuggingFaceEmbeddings object
    based on the specified model name.
    
    Args:
        model_name (str): The name of the Hugging Face model to use for embeddings.
                          Default is "sentence-tranformers/all-MiniLM-L6-v2".
    
    Returns:
        HuggingFaceEmbeddings: An instance of HuggingFaceEmbeddings initialized with the specified model.
    """
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    return embeddings