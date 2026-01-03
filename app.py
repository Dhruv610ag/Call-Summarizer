"""from audio_extractor import transcribe_audio_simple
from sentimentanalyser import SentimentAnalyzer

def run_pipeline(audio_path: str):
    print("Starting Call Analysis Pipeline...")

    # Step 1: Speech → Text
    transcript = transcribe_audio_simple(audio_path)

    # Step 2: Sentiment Analysis
    sentiment_model = SentimentAnalyzer()
    sentiment = sentiment_model.analyze(transcript)

    return {
        "transcript": transcript,
        "sentiment": sentiment
    }


if __name__ == "__main__":
    audio_file = "sample_testing.wav"
    output = run_pipeline(audio_file)

    print("\nFinal Output:")
    print(output)
"""