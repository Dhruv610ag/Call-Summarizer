from audio_extractor import transcribe_audio_simple
from langchain.text_splitter import RecursiveCharacterTextSplitter


def text_extractor(audio_file_path):
    """
    Extracts text from an audio file using Whisper model.
    
    Args:
        audio_file_path (str): Path to the audio file.
        model_size (str): Size of the Whisper model to use. Default is "medium".
        
    Returns:
        str: Transcribed text from the audio file.
    """
    transcript=transcribe_audio_simple(audio_file_path)
    return transcript

def length_extracted_text(transcript):
    """
    Return the length of the extracted text from the audio file.
    """
    return len(transcript)

def split_extracted_text(transcript):
    """
    Splits the extracted text in smaller chunks for preprocessing.
    """
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        separators=["\n\n","\n","."," "]
    )
    text_chunks=text_splitter.split_text(transcript)
    return text_chunks