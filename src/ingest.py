import os
import shutil
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_community.vectorstores import FAISS

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INDEX_DIR = BASE_DIR / "index"

PROVIDER = os.getenv("PROVIDER", "openai").lower()


def get_embeddings():
    if PROVIDER == "ollama":
        from langchain_ollama import OllamaEmbeddings
        return OllamaEmbeddings(model="nomic-embed-text")
    from langchain_openai import OpenAIEmbeddings
    return OpenAIEmbeddings(model="text-embedding-3-small")


def main():
    print(f"Provider: {PROVIDER}")
    splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[("#", "title"), ("##", "section")]
    )

    chunks = []
    for path in sorted(DATA_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for part in splitter.split_text(text):
            title = part.metadata.get("title", "")
            section = part.metadata.get("section", "")
            if not section:
                continue  # skip the bare title line
            # Put the heading into the text so search knows the context
            content = f"{title} - {section}\n{part.page_content}"
            chunks.append(Document(
                page_content=content,
                metadata={"source": path.name, "section": section},
            ))

    if not chunks:
        print("No chunks created. Check the data folder.")
        return
    print(f"Created {len(chunks)} chunks from {len(list(DATA_DIR.glob('*.md')))} files")

    if INDEX_DIR.exists():
        shutil.rmtree(INDEX_DIR)
    db = FAISS.from_documents(chunks, get_embeddings())
    db.save_local(str(INDEX_DIR))
    print(f"Index saved to {INDEX_DIR}")


if __name__ == "__main__":
    main()