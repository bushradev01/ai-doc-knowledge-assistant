# Stakeholder Research & Market Analysis

**Project:** AI Document Knowledge Assistant & Q&A App
**Author:** Bushra Ashraf, Khadija Malik
**Date:** 12 October 2026

---

## 1. Research Method

**Important note:** I did not have access to participants for live interviews.
Instead, I created **4 synthetic user personas** that reflect common
patterns reported in developer surveys and online discussions about
documentation search and AI assistants. The persona answers below are
**simulated, not real interview responses.** They will be validated in
Week 3 through testing with real users.

I also reviewed existing tools by trying them myself (Section 3).

---

## 2. Synthetic User Personas

| Persona | Role | How they search now | Time spent | Biggest frustration | Trust factor | Speed expected |
|---|---|---|---|---|---|---|
| P1: Ayesha | Junior developer | Ctrl+F in docs, then Google, then asks a senior | 15-30 min | Docs use different words than she searches for | Wants a link to the exact page | Under 5 sec |
| P2: Hamza | Senior developer | Doc site search, then reads source code | 10-20 min | Docs are outdated or split across many pages | Wants the source file and section named | Under 3 sec |
| P3: Sara | Customer support agent | Searches the FAQ, then asks teammates | 5-15 min per ticket | Cannot find answers during live chats | Wants an answer she can quote to a customer | Under 2 sec |
| P4: Bilal | New employee | Asks colleagues, browses the wiki | 30+ min | Does not know which document to open | Wants proof the answer is current | Under 5 sec |

### Key findings
- Keyword search fails when users word things differently than the docs.
- All four personas want the source shown before they trust an answer.
- Time lost searching is 10 to 30 minutes per question, and colleagues are interrupted.
- Fast response matters most for live work such as support.
- Users distrust AI that sounds confident but gives no evidence.

---

## 3. Existing Tools Review

**Test question used:** (write one question from your own document set, for example "How do I reset my password?")

| Tool | Strengths | Weaknesses | Citations? | Speed |
|---|---|---|---|---|
| ChatGPT with file upload | Natural language answers, easy to use | Citations can be vague, limited to uploaded files, not embeddable in a company site | Partial | 3-10 sec |
| NotebookLM | Shows citations linked to passages | Not customizable, cannot be embedded in your own app | Yes | 3-8 sec |
| Docs site search bar | Fast, shows page links | Only matches keywords, gives no direct answer | Page links only | Under 1 sec |
| Generic chatbot (no documents) | Fast and fluent | Does not know company docs, may invent answers | No | 2-5 sec |

**Note:** Replace the strengths, weaknesses and speed with what you see when
you try each tool.

### Key findings
- Docs search is fast but cannot answer in plain language.
- General AI tools answer well but are not tied to your own documents or reliable citations.
- **Gap:** an assistant limited to the company's own docs that answers in plain language, shows exact sources, and says "I don't know" when unsure.

---

## 4. Requirements

| ID | Requirement | Reason (from research) | Priority |
|---|---|---|---|
| R1 | Every answer shows source citations (file name and section) | All personas need to verify answers | High |
| R2 | Answers appear in under 2 seconds on average | Support use needs speed; matches project benchmark | High |
| R3 | The assistant says "I don't know" when the docs lack the answer | Fear of invented answers | High |
| R4 | Accept questions in natural language | Keyword search fails on different wording | High |
| R5 | Answer only from the provided documents | Avoids wrong generic answers | High |
| R6 | Simple chat interface | New users need an easy start | Medium |
| R7 | Allow new documents to be added | Docs change often | Medium |
| R8 | Show which document version or file was used | Helps users judge if info is outdated | Low |