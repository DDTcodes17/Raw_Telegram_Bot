import os
from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model

gemini_key = os.getenv("GOOGLE_API_KEY")


gemini_llm = init_chat_model(
    model = "gemini-3.1-flash-lite",
    model_provider="google-genai"   
)
