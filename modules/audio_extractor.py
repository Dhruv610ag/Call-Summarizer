import whisper
from pydub import AudioSegment
import warnings
import os
warnings.filterwarnings("ignore", category=UserWarning)

_MODEL_CACHE={}

def get_whisper_model(model_size):
    if model_size not in _MODEL_CACHE:
        print(f"Loading Whisper model: {model_size}")
        _MODEL_CACHE[model_size] = whisper.load_model(model_size)
    return _MODEL_CACHE[model_size]


def convert_to_wav(input_file_path, output_file_path):
    """
    Converts an audio file to WAV format.
    Args:
        input_file_path (str): Path to the input audio file.
        output_file_path (str): Path to save the converted WAV file.
    """
    try:
        audio = AudioSegment.from_file(input_file_path)
        audio.export(output_file_path, format="wav")
    except Exception as e:
        raise RuntimeError(f"Audio conversion failed: {e}")
    
def transcribe_audio_simple(audio_file_path, model_size="medium"):
    """
    this function transcribes audio using the whisper "medium" model  by default.
    Args:
        audio_file_path (str): Path to the audio file to be transcribed.
        model_size (str): Size of the Whisper model to use. Default is "medium".
    Returns:
        str:Transcribed text from the audio file.
    """
    if model_size not in ["tiny", "base", "small", "medium", "large"]:
        raise ValueError("Invalid model size.")

    if not audio_file_path.lower().endswith(".wav"):
        wav_file_path = audio_file_path.rsplit(".", 1)[0] + ".wav"
        if not os.path.exists(wav_file_path):
            print(f"Converting {audio_file_path} to WAV...")
            convert_to_wav(audio_file_path, wav_file_path)
        audio_file_path = wav_file_path

    model = get_whisper_model(model_size)
    print("Transcribing audio...")
    result = model.transcribe(audio_file_path)
    return result["text"]

print(transcribe_audio_simple(r"C:\Users\DHRUV AGARWAL\Desktop\Call-Summarizer\testing_audios\sample_testing.wav"))

    