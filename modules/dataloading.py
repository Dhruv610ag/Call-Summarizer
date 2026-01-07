from modules.audio_extractor import transcribe_audio_simple
from langchain.text_splitter import RecursiveCharacterTextSplitter


def text_extractor(audio_file_path):
    """
    Extracts text from an audio file using Whisper model.
    """
    transcript = transcribe_audio_simple(audio_file_path)
    return transcript

def length_extracted_text(transcript):
    """
    Return the character length of the extracted text.
    """
    return len(transcript)

def split_extracted_text(transcript):
    """
    Splits the extracted text into smaller chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " "]
    )
    return text_splitter.split_text(transcript)
