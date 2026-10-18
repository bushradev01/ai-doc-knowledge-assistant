# Core Framework Draft

**Project:** AI Document Knowledge Assistant & Q&A App
**Authors:** Bushra, Khadija
**Date:** 18th october, 2026

## 1. Overview
A RAG (Retrieval-Augmented Generation) pipeline: find the most relevant
parts of the documents first, then ask the model to answer only from them.

## 2. Workflow

Indexing (done once, or when documents change):
Markdown files -> Split into chunks -> Create embeddings -> Save in FAISS index

Answering (done for every question):
User question -> Embed question -> Find top 3 similar chunks (FAISS)
-> Build prompt with chunks -> LLM answers -> Show answer + sources + time

## 3. Components

| Component | Tool | Role | File |
|---|---|---|---|
| Loader | Python (pathlib) | Reads .md files, stores file name as source | src/ingest.py |
| Splitter | LangChain RecursiveCharacterTextSplitter | Cuts text into chunks | src/ingest.py |
| Embeddings | OpenAI embeddings | Turns text into vectors | src/ingest.py |
| Vector store | FAISS | Finds similar chunks | index/ |
| LLM | OpenAI gpt-4o-mini | Writes the answer | src/qa.py |
| Interface | Streamlit | Chat page (Week 3) | src/app.py |

## 4. Settings

| Setting | Value | Reason |
|---|---|---|
| Chunk size | 500 characters | Small enough to be precise |
| Chunk overlap | 50 | Keeps sentences from being cut off |
| Chunks retrieved (k) | 3 | Balance of accuracy and speed |
| Model | gpt-4o-mini | Low cost, fast |
| Temperature | 0 | Stable, less invented content |

## 5. Rules built into the prompt
- Answer only from the provided context.
- If the answer is not there, say "I don't know based on the provided documents."
- Show the source file for every answer.

## 6. Known limits (to improve in Week 3)
- Sources shown are the retrieved files, not a guarantee they were all used.
- Citations show file names only, not sections.
- No chat memory between questions.
- Tested only on a small sample set.

## 7. Link to requirements
R1 citations: sources shown. R3 "I don't know": prompt rule.
R4 natural language: embeddings. R5 only from docs: prompt rule.