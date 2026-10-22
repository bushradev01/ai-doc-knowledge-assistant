import os
import time
from pathlib import Path

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
INDEX_DIR = BASE_DIR / "index"

PROVIDER = os.getenv("PROVIDER", "openai").lower()
CHAT_MODEL = os.getenv("CHAT_MODEL", "qwen2.5:0.5b")  # set to the model you use
# Lower score = better match. Leave empty at first, tune after the pilot.
MAX_DISTANCE = float(os.getenv("MAX_DISTANCE", "0")) or None
RETRIEVE_K = 3
CITE_TOP = 1
IDK = "I don't know based on the provided documents."

PROMPT = """You are a documentation assistant.
Answer the question using ONLY the context below.
If the answer is not in the context, reply exactly: "I don't know based on the provided documents."
Do not use outside knowledge. Keep the answer short and clear.

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
        return ChatOllama(model=CHAT_MODEL, temperature=0)
    from langchain_openai import ChatOpenAI
    return ChatOpenAI(model="gpt-4o-mini", temperature=0)


db = FAISS.load_local(
    str(INDEX_DIR), get_embeddings(), allow_dangerous_deserialization=True
)
llm = get_llm()


def ask(question, k=RETRIEVE_K):
    """Return answer, citations (file > section), match scores and time."""
    start = time.time()
    results = db.similarity_search_with_score(question, k=k)  # sorted best first
    scores = [round(float(s), 3) for _, s in results]

    # Optional cutoff: if even the best match is too far, do not call the model
    if MAX_DISTANCE and scores and scores[0] > MAX_DISTANCE:
        return {"answer": IDK, "sources": [], "scores": scores,
                "seconds": round(time.time() - start, 2)}

    context = "\n\n".join(doc.page_content for doc, _ in results)
    answer = llm.invoke(PROMPT.format(context=context, question=question)).content.strip()

    sources = []
    if "don't know" not in answer.lower():
        for doc, _ in results[:CITE_TOP]:
            label = f"{doc.metadata['source']} > {doc.metadata.get('section', '')}"
            if label not in sources:
                sources.append(label)

    return {"answer": answer, "sources": sources, "scores": scores,
            "seconds": round(time.time() - start, 2)}


if __name__ == "__main__":
    print(f"Provider: {PROVIDER}, model: {CHAT_MODEL}")
    while True:
        q = input("\nQuestion (or 'quit'): ").strip()
        if q.lower() == "quit":
            break
        if not q:
            continue
        r = ask(q)
        print("Answer:", r["answer"])
        print("Sources:", ", ".join(r["sources"]) or "none")
        print("Scores:", r["scores"])
        print("Time:", r["seconds"], "sec")