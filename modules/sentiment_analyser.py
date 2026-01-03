import os
import warnings
from dotenv import load_dotenv
import google.generativeai as genai

from prompt import system_prompt  # ✅ using your existing prompt

warnings.filterwarnings("ignore")

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("Gemini_API_Key")

if GEMINI_API_KEY is None:
    raise EnvironmentError("Gemini_API_Key not found in .env file")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)


class CallSummarizer:
    """
    Final Summarization stage of the Call Intelligence Pipeline
    Uses pre-defined system prompt from prompt.py
    """

    def __init__(self, model_name: str = "gemini-1.5-flash"):
        print("Loading Gemini summarization model...")
        self.model = genai.GenerativeModel(model_name)

    def summarize(
        self,
        transcript: str,
        retrieved_context: str = ""
    ) -> str:
        """
        Generate an executive-level call summary.

        Args:
            transcript (str): Whisper-generated transcript
            retrieved_context (str): Context retrieved from vector DB (optional)

        Returns:
            str: Structured call summary
        """

        if not transcript or transcript.strip() == "":
            raise ValueError("Transcript is empty. Cannot summarize.")

        prompt = self._build_prompt(
            transcript=transcript,
            retrieved_context=retrieved_context
        )

        response = self.model.generate_content(prompt)
        return response.text.strip()

    def _build_prompt(self, transcript: str, retrieved_context: str) -> str:
        """
        Injects retrieved context into the system prompt
        """

        context_block = (
            f"Retrieved Context:\n{retrieved_context}"
            if retrieved_context else
            "Retrieved Context:\nNone"
        )

        final_prompt = system_prompt.format(Context=context_block)

        final_prompt += f"""

Call Transcript:
\"\"\"
{transcript}
\"\"\"

Generate the call summary following the system instructions above.
"""

        return final_prompt


