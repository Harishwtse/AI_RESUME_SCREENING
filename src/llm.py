from langchain_groq import ChatGroq
from src.config import GROQ_API_KEY, MODEL
def get_llm():
    if not GROQ_API_KEY:
        raise RuntimeError("Set GROQ_API_KEY in .env")
    return ChatGroq(api_key=GROQ_API_KEY, model=MODEL, temperature=0)
