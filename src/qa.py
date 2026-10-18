import os
import time
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
INDEX_DIR = BASE_DIR / "index"

PROVIDER = os.getenv("PROVIDER", "openai").lower()

PROMPT = """You are a documentation assistant.
Answer the question using ONLY the context below.
If the answer is not in the context, reply exactly: "I don't know based on the provided documents."
Keep the answer short and clear.

Context:
{context}

Question: {question}

Answer:"""


def get_embeddings():
    if PROVIDER == "ollama":
        from langchain_ollama import OllamaEmbeddings
        return OllamaEmbeddings(model="nomic-embed-text")
    from langchain_openai import OpenAIEmbeddings
    return OpenAIEmbeddings(model="text-embedding-3-small")


def get_llm():
    if PROVIDER == "ollama":
        from langchain_ollama import ChatOllama
        return ChatOllama(model="qwen2.5:0.5b", temperature=0)
    from langchain_openai import ChatOpenAI
    return ChatOpenAI(model="gpt-4o-mini", temperature=0)


db = FAISS.load_local(
    str(INDEX_DIR), get_embeddings(), allow_dangerous_deserialization=True
)
llm = get_llm()


def ask(question, k=3):
    """Return the answer, the source files and the time taken."""
    start = time.time()
    results = db.similarity_search(question, k=k)
    context = "\n\n".join(r.page_content for r in results)
    answer = llm.invoke(PROMPT.format(context=context, question=question)).content
    sources = sorted({r.metadata["source"] for r in results})
    return {
        "answer": answer.strip(),
        "sources": sources,
        "seconds": round(time.time() - start, 2),
    }


if __name__ == "__main__":
    print(f"Provider: {PROVIDER}")
    while True:
        q = input("\nQuestion (or 'quit'): ").strip()
        if q.lower() == "quit":
            break
        if not q:
            continue
        r = ask(q)
        print("Answer:", r["answer"])
        print("Sources:", ", ".join(r["sources"]))
        print("Time:", r["seconds"], "sec")