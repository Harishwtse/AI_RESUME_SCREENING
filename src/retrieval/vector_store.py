# Optional FAISS index for semantic job/resume text retrieval.
from langchain_community.vectorstores import FAISS
from src.retrieval.embeddings import get_embeddings
def build_index(texts):
    return FAISS.from_texts(texts, get_embeddings())
