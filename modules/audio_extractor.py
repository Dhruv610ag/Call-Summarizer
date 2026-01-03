import whisper
from pydub import AudioSegment
import warnings
warnings.filterwarnings("ignore")

def convert_to_wav(input_file_path, output_file_path):
    """
    Converts an audio file to WAV format.
    Args:
        input_file_path (str): Path to the input audio file.
        output_file_path (str): Path to save the converted WAV file.
    """
    audio = AudioSegment.from_file(input_file_path)
    audio.export(output_file_path, format="wav")
    
def transcribe_audio_simple(audio_file_path,model_size="medium"):
    """
    this function transcribes audio using the whisper "medium" model  by default.
    Args:
        audio_file_path (str): Path to the audio file to be transcribed.
        model_size (str): Size of the Whisper model to use. Default is "medium".
    Returns:
        str:Transcribed text from the audio file.
    """
    print(f"Loding the model: {model_size}")
    if model_size not in ["tiny","base","small","medium","large"]:
        raise ValueError("Invalid model size. Choose from 'tiny', 'base', 'small', 'medium', 'large'.")
    model=whisper.load_model(model_size)
    if not audio_file_path.lower().endswith('.wav'):
        wav_file_path=audio_file_path.rsplit('.',1)[0]+'.wav'
        print(f"Converting {audio_file_path} to WAV format at {wav_file_path}")
        convert_to_wav(audio_file_path,wav_file_path)
        audio_file_path=wav_file_path
    print("Transcripting the audio_file to the simple text format ...")
    result=model.transcribe(audio_file_path)    
    return result["text"]
print(transcribe_audio_simple(r"C:\Users\Ayush Sharma\OneDrive\Desktop\Call-Summarizer\testing_audios\sample_testing.wav"))
    