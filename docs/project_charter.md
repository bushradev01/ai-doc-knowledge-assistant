# Project Charter & KPI Document

**Project:** AI Document Knowledge Assistant & Q&A App
**Author:** Bushra Ashraf, Khadija Malik
**Date:** 12 October 2026
**Duration:** 4 weeks

---

## 1. Goal
Build an interactive Retrieval-Augmented Generation (RAG) assistant that
answers questions from custom documentation in natural language, shows
source citations, and responds in under 2 seconds.

## 2. Problem Statement
In the example scenario (Acme Cloud Intelligence), employees and trial users
spend 10 to 30 minutes per question searching 200+ markdown docs and FAQs.
Keyword search misses differently worded questions, answers are scattered
across files, and generic AI tools give answers without verifiable sources.
See `baseline_audit_report.md` and `market_research.md`.

## 3. Scope

### In scope
- Load and index markdown documents
- Natural language question answering over those documents
- Source citations (file name and section) on every answer
- "I don't know" response when the docs lack the answer
- Streamlit web interface
- Testing on a set of about 30 questions
- Deployment and final report

### Out of scope
- User login and accounts
- Support for non-text files such as images and video
- Multi-language support
- Training or fine-tuning a custom model
- Real-time syncing with external document systems

## 4. Requirements
Summarised from `market_research.md`:

| ID | Requirement | Priority |
|---|---|---|
| R1 | Every answer shows source citations | High |
| R2 | Average response time under 2 seconds | High |
| R3 | Says "I don't know" when docs lack the answer | High |
| R4 | Accepts natural language questions | High |
| R5 | Answers only from the provided documents | High |
| R6 | Simple chat interface | Medium |
| R7 | New documents can be added | Medium |
| R8 | Shows which file was used | Low |

## 5. Success Metrics (KPIs)

| KPI | Target | How it is measured | Baseline |
|---|---|---|---|
| Response time | Under 2 seconds on average | Timer in the app, averaged over the test set | Manual search: 10 to 30 min |
| Citation coverage | 100% of answers show a citation | Check every test answer | Not available today |
| Answer accuracy | 85% or more correct | Score about 30 test questions with known answers | Not measured |
| Refusal quality | 90% of out-of-scope questions get "I don't know" | Test with 5 to 10 questions not in the docs | Not measured |
| Usability | Average 4 out of 5 from test users | Short feedback form in Week 3 | Not measured |

## 6. Timeline

| Week | Focus | Output |
|---|---|---|
| 1 | Scope definition and baseline analysis | Audit report, charter, workspace |
| 2 | Build the RAG pipeline | Document loading, embeddings, FAISS index, cited answers |
| 3 | Improve and test | Streamlit interface, 30-question test, KPI measurement |
| 4 | Deploy and report | Live app, final report, demo |

## 7. Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Model gives wrong or invented answers | Medium | High | Strict prompt to use only retrieved text, "I don't know" rule, accuracy testing |
| Responses slower than 2 seconds | Medium | High | Smaller chunks, fewer retrieved results, a fast model, caching the index |
| OpenAI API cost grows | Low | Medium | Use a low-cost model, set a spending limit, cache results |
| Poor retrieval because of bad chunking | Medium | High | Test different chunk sizes and overlap in Week 3 |
| API key leaked | Low | High | Keep the key in `.env`, which is in `.gitignore` |
| Research is based on simulated personas | High | Medium | Validate with real users in Week 3 |

## 8. Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Project owner | Bushra Ashraf, Khadija Malik | Approved | 18 October 2026 |
| Reviewer / mentor | Hania Akbar, Arooj Saleem (Reviewer) | Approved | |

*Scope approved by the project owner. Reviewer sign-off to be added when received.*