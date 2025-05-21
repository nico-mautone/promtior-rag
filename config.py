import os
from dotenv import load_dotenv

load_dotenv()

CHUNK_SIZE: int = 750
CHUNK_OVERLAP: int = 100

PERSIST_DIR: str = "store"

# ---------- embedding ----------
EMBEDDING_MODEL: str = "text-embedding-3-small"
LLM_MODEL: str = "gpt-4.1-nano-2025-04-14"
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

# ---------- data sources ----------
PROMTIOR_URLS: list[str] = [
    "https://www.promtior.ai/",
    "https://www.promtior.ai/service",
    "https://www.promtior.ai/use-cases",
    "https://www.promtior.ai/contacto",
    "https://www.promtior.ai/blog"
]
PROMTIOR_PDF: str = "assets/AI_engineer.pdf"