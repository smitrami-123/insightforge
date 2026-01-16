import os

# ---- App / UI ----
APP_TITLE = "InsightForge: News Research Tool 📈"
SIDEBAR_TITLE = "Article URLs"
MAX_URLS = 3

# ---- Index ----
INDEX_DIR = os.getenv("INSIGHTFORGE_INDEX_DIR", "insightforge_faiss_index")

# ---- Chunking ----
CHUNK_SIZE = int(os.getenv("INSIGHTFORGE_CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("INSIGHTFORGE_CHUNK_OVERLAP", "150"))
SEPARATORS = ["\n\n", "\n", ".", ","]

# ---- Retrieval ----
TOP_K = int(os.getenv("INSIGHTFORGE_TOP_K", "4"))

# ---- Models ----
EMBEDDING_MODEL = os.getenv("INSIGHTFORGE_EMBEDDING_MODEL", "text-embedding-3-small")
CHAT_MODEL = os.getenv("INSIGHTFORGE_CHAT_MODEL", "gpt-5.1")
TEMPERATURE = float(os.getenv("INSIGHTFORGE_TEMPERATURE", "0.2"))

# ---- Safety ----
# Safe if you created the index locally. Keep True for local dev; consider stricter handling for shared environments.
ALLOW_DANGEROUS_DESERIALIZATION = True
