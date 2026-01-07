import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import warnings
warnings.filterwarnings("ignore")
load_dotenv()

GEMINI_API_KEY = os.getenv("Gemini_API_Key")

if GEMINI_API_KEY is None:
    raise EnvironmentError("Gemini_API_Key not found in .env file")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)


class CallSummarizer:
    """
    Call Summarizer using Gemini LLM
    Final stage of the Call Summarization pipeline
    """

    def __init__(self, model_name: str = "gemini-1.5-flash"):
        print("Loading Gemini summarization model...")
        self.model = genai.GenerativeModel(model_name)

    def summarize(
        self,
        transcript: str,
        sentiment: dict = None,
        retrieved_context: str = None
    ) -> str:
        """
        Generate a structured summary of a call.

        Args:
            transcript (str): Whisper-generated transcript
            sentiment (dict): Output of SentimentAnalyzer
            retrieved_context (str): Context from RAG (optional)

        Returns:
            str: Call summary
        """

        if not transcript or transcript.strip() == "":
            raise ValueError("Transcript is empty. Cannot summarize.")

        prompt = self._build_prompt(
            transcript=transcript,
            sentiment=sentiment,
            retrieved_context=retrieved_context
        )

        response = self.model.generate_content(prompt)
        return response.text.strip()

    def _build_prompt(self, transcript, sentiment, retrieved_context):
        """
        Builds a robust, RAG-aware summarization prompt
        """

        sentiment_block = ""
        if sentiment:
            sentiment_block = (
                f"\nCustomer Sentiment:\n"
                f"- Overall Sentiment: {sentiment.get('sentiment')}\n"
                f"- Confidence Score: {sentiment.get('confidence')}\n"
            )

        context_block = ""
        if retrieved_context:
            context_block = (
                "\nRelevant Retrieved Context (for grounding):\n"
                f"{retrieved_context}\n"
            )

        prompt = f"""
You are an AI assistant specialized in call center analytics.

Your task is to generate a **clear, professional, and factual summary**
of the following customer support call.

{sentiment_block}

{context_block}

Call Transcript:
\"\"\"
{transcript}
\"\"\"

Generate the summary in the following format:

1. Call Purpose
2. Key Issues Discussed
3. Actions Taken by Agent
4. Customer Sentiment Overview
5. Final Outcome / Resolution Status

Guidelines:
- Do NOT hallucinate information
- Base the summary strictly on the transcript and provided context
- Keep the tone professional and concise
"""

        return prompt



