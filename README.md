# AI Document Knowledge Assistant & Q&A App

A Retrieval-Augmented Generation (RAG) assistant that answers questions
from custom documentation and shows source citations.

## Tools
Python, LangChain, OpenAI API, FAISS, Streamlit

## 4-Week Plan
- Week 1: Scope definition and baseline analysis
- Week 2: Build the RAG pipeline
- Week 3: Improve and test
- Week 4: Deploy and report

## Folder Structure
- `docs/` audit report, charter, KPIs
- `data/` sample documents
- `src/` code

## Links
- Project master sheet: https://docs.google.com/spreadsheets/d/1orztmFp4pMQ89cbd1EQpyS8GUpTHMXOBTvOjyY3AF3c/edit?usp=sharing

## Team
- Bushra Ashraf 
- Khadija Malik

## Week 1 Deliverables
- [Baseline Audit Report](docs/baseline_audit_report.md)
- [Market Research & Requirements](docs/market_research.md)
- [Project Charter & KPIs](docs/project_charter.md)
- [Project Master Sheet]: https://docs.google.com/spreadsheets/d/1orztmFp4pMQ89cbd1EQpyS8GUpTHMXOBTvOjyY3AF3c/edit?usp=sharing

## Week 2 Deliverables
- [Core Framework Draft](docs/framework_design.md)
- [Templates & Guidelines](docs/templates/)
- [Test Scenario Log](docs/test_scenario_log.md)
- [Feedback Log](docs/feedback.md)
- Code: `src/ingest.py`, `src/qa.py`, `src/run_tests.py`

## How to Run
1. Create a virtual environment and run `pip install -r requirements.txt`
2. Install Ollama, then run `ollama pull nomic-embed-text` and `ollama pull qwen2.5:0.5b`
3. Create a `.env` file with `PROVIDER=ollama`
4. Build the index: `python src\ingest.py`
5. Ask questions: `python src\qa.py`
6. Run the test log: `python src\run_tests.py`

## Notes
- The pipeline runs on local Ollama models because the OpenAI account had no API credit. Switching to OpenAI needs `PROVIDER=openai` and an API key in `.env`, then re-running `ingest.py`.
- Sample documents in `data/` were written for this project.
- Known limits: sources shown are all retrieved files, and the small local model is less accurate. Both are planned for improvement in Week 3.