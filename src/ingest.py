import os
import shutil
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INDEX_DIR = BASE_DIR / "index"

PROVIDER = os.getenv("PROVIDER", "openai").lower()


def get_embeddings():
    """Return the embedding model for the chosen provider."""
    if PROVIDER == "ollama":
        from langchain_ollama import OllamaEmbeddings
        return OllamaEmbeddings(model="nomic-embed-text")
    from langchain_openai import OpenAIEmbeddings
    return OpenAIEmbeddings(model="text-embedding-3-small")


def main():
    print(f"Provider: {PROVIDER}")

    # 1. Load every markdown file
    docs = []
    for path in sorted(DATA_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        docs.append(Document(page_content=text, metadata={"source": path.name}))
    if not docs:
        print("No .md files found in the data folder.")
        return
    print(f"Loaded {len(docs)} documents")

    # 2. Split into chunks (file name is kept as the source)
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    # 3. Embed and save the index (old index is replaced)
    if INDEX_DIR.exists():
        shutil.rmtree(INDEX_DIR)
    db = FAISS.from_documents(chunks, get_embeddings())
    db.save_local(str(INDEX_DIR))
    print(f"Index saved to {INDEX_DIR}")


if __name__ == "__main__":
    main()