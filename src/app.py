import re
from pathlib import Path

import streamlit as st
from qa import ask, PROVIDER, CHAT_MODEL, MAX_DISTANCE, CITE_TOP, RETRIEVE_K

BASE = Path(__file__).resolve().parent.parent
DOCS = BASE / "docs"
DATA = BASE / "data"

st.set_page_config(page_title="Acme Docs Assistant", page_icon="📚", layout="wide")

st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 55%, #06b6d4 100%);
    padding: 28px 32px; border-radius: 18px; color: white; margin-bottom: 18px;
}
.hero h1 { color: white; margin: 0 0 6px 0; font-size: 2.1rem; }
.hero p { color: #e0e7ff; margin: 0; font-size: 1.02rem; }
.chip {
    display: inline-block; padding: 3px 12px; margin: 6px 6px 0 0;
    border-radius: 999px; font-size: 0.82rem;
    background: rgba(99,102,241,0.14); color: #4f46e5;
    border: 1px solid rgba(99,102,241,0.35);
}
.chip-hero {
    background: rgba(255,255,255,0.18); color: white;
    border: 1px solid rgba(255,255,255,0.35);
}
.card {
    border: 1px solid rgba(128,128,128,0.25); border-radius: 14px;
    padding: 14px 18px; margin-bottom: 12px;
    background: rgba(128,128,128,0.06);
}
.card h4 { margin: 0 0 6px 0; }
</style>
""", unsafe_allow_html=True)

EXAMPLES = [
    "How do I reset my password?",
    "When do backups run?",
    "How much is the Business plan?",
    "What is the API rate limit on the Starter plan?",
    "How is data encrypted at rest?",
    "Who is the CEO of Acme Cloud?",
]

if "history" not in st.session_state:
    st.session_state.history = []
    st.session_state.times = []


def run_question(q):
    with st.spinner("Searching the documents..."):
        try:
            r = ask(q)
        except Exception as e:
            r = {"answer": f"Something went wrong: {e}", "sources": [],
                 "scores": [], "seconds": 0}
    st.session_state.history.append({"q": q, **r})
    st.session_state.times.append(r["seconds"])


def pilot_summary(label):
    f = DOCS / f"pilot_{label}.md"
    if not f.exists():
        return None
    text = f.read_text(encoding="utf-8")
    if "## Summary" not in text:
        return None
    return [l[2:] for l in text.split("## Summary")[1].splitlines() if l.startswith("- ")]


# ---------- Handle input FIRST so the sidebar shows fresh numbers ----------
typed = st.chat_input("Ask a question about the documentation...")
question = typed or st.session_state.pop("pending", None)
if question:
    run_question(question)

# ---------- Sidebar ----------
with st.sidebar:
    st.header("📈 Project progress")
    st.markdown(
        "✅ **Week 1** Scope, research, charter  \n"
        "✅ **Week 2** RAG pipeline, test log  \n"
        "🔄 **Week 3** App, pilot, SLA (now)  \n"
        "⬜ **Week 4** Deploy, report, demo"
    )
    st.divider()
    st.header("⏱ Session stats")
    if st.session_state.times:
        avg = sum(st.session_state.times) / len(st.session_state.times)
        c1, c2 = st.columns(2)
        c1.metric("Questions", len(st.session_state.times))
        c2.metric("Avg sec", round(avg, 2))
    else:
        st.caption("No questions yet.")
    if st.button("🗑 Clear chat", use_container_width=True):
        st.session_state.history = []
        st.session_state.times = []
        st.rerun()

# ---------- Header ----------
n_docs = len(list(DATA.glob("*.md")))
st.markdown(f"""
<div class="hero">
  <h1>📚 Document Knowledge Assistant</h1>
  <p>Ask a question in plain English. Answers come only from the documentation,
  and every answer shows its source.</p>
  <span class="chip chip-hero">🧠 {CHAT_MODEL}</span>
  <span class="chip chip-hero">⚙️ {PROVIDER}</span>
  <span class="chip chip-hero">📄 {n_docs} documents</span>
  <span class="chip chip-hero">🔎 FAISS search</span>
</div>
""", unsafe_allow_html=True)

tab_ask, tab_guide, tab_pilot = st.tabs(["💬 Ask", "🧭 Project Guide", "📊 Pilot Results"])

# ---------- Tab 1: Ask ----------
with tab_ask:
    if not st.session_state.history:
        st.markdown("#### 👋 Try one of these questions")
        cols = st.columns(3)
        for i, ex in enumerate(EXAMPLES):
            if cols[i % 3].button(ex, key=f"ex{i}", use_container_width=True):
                st.session_state.pending = ex
                st.rerun()
        st.caption("Or type your own question in the box at the bottom.")

    for item in st.session_state.history:
        with st.chat_message("user"):
            st.write(item["q"])
        with st.chat_message("assistant"):
            if "don't know" in item["answer"].lower():
                st.warning(item["answer"])
            else:
                st.success(item["answer"])
            chips = "".join(f'<span class="chip">📄 {s}</span>' for s in item["sources"])
            if chips:
                st.markdown(chips, unsafe_allow_html=True)
            best = item.get("scores", [])
            extra = f" · best match score {best[0]}" if best else ""
            st.caption(f"⏱ {item['seconds']} sec{extra}")

# ---------- Tab 2: Project Guide ----------
with tab_guide:
    st.markdown("### What this project is")
    st.write(
        "A Retrieval-Augmented Generation (RAG) assistant. Instead of letting an AI "
        "guess, it first finds the most relevant parts of the documents, then answers "
        "only from them and shows where the answer came from."
    )

    st.markdown("### How an answer is made")
    s1, s2, s3, s4 = st.columns(4)
    s1.markdown('<div class="card"><h4>1️⃣ Ask</h4>You type a question.</div>', unsafe_allow_html=True)
    s2.markdown('<div class="card"><h4>2️⃣ Search</h4>FAISS finds the closest document sections. If none is close enough, the assistant refuses.</div>', unsafe_allow_html=True)
    s3.markdown('<div class="card"><h4>3️⃣ Answer</h4>The local model answers using only those sections.</div>', unsafe_allow_html=True)
    s4.markdown('<div class="card"><h4>4️⃣ Cite</h4>The file and section are shown as the source.</div>', unsafe_allow_html=True)

    st.markdown("### What we have done")
    a, b, c = st.columns(3)
    a.markdown(
        '<div class="card"><h4>✅ Week 1</h4>Baseline audit report, market research '
        '(simulated personas), project charter with KPIs, GitHub repo and master sheet.</div>',
        unsafe_allow_html=True)
    b.markdown(
        '<div class="card"><h4>✅ Week 2</h4>Indexing and Q&A scripts, local Ollama models, '
        '10-question test log, framework document, templates, feedback.</div>',
        unsafe_allow_html=True)
    c.markdown(
        '<div class="card"><h4>🔄 Week 3 (now)</h4>This Streamlit app, section-level '
        'citations, a 30-question pilot run before and after changes, SLA checklist.</div>',
        unsafe_allow_html=True)

    st.markdown("### Settings in use")
    st.table({
        "Setting": ["Chat model", "Chunks retrieved (k)", "Sources cited", "Distance cutoff (MAX_DISTANCE)"],
        "Value": [CHAT_MODEL, str(RETRIEVE_K), str(CITE_TOP),
                  str(MAX_DISTANCE) if MAX_DISTANCE else "not set"],
    })

    st.markdown("### Changes made from pilot data")
    st.markdown(
        "- **Sources cited 2 → 1:** an irrelevant file appeared as a source for the password question\n"
        "- **Distance cutoff added:** run 1 showed invented answers for questions not in the documents\n"
        "- **Cutoff chosen from run 1 scores:** just above the highest score of a valid question"
    )

    st.markdown("### What we are doing next")
    st.markdown(
        "- Run the pilot again and compare before and after\n"
        "- Collect live feedback from 3 users\n"
        "- Finish the SLA checklist\n"
        "- **Week 4:** deploy the app, write the final report, record the demo"
    )

    st.markdown("### Documents the assistant knows")
    for f in sorted(DATA.glob("*.md")):
        st.markdown(f'<span class="chip">📄 {f.name}</span>', unsafe_allow_html=True)

    st.markdown("### Known limits (honest list)")
    st.markdown(
        "- A small local model is less accurate than a large cloud model\n"
        "- The sample documents were written for this project\n"
        "- One distance cutoff cannot perfectly separate valid from out-of-scope questions\n"
        "- The cutoff was tuned on the same 30 pilot questions, so real accuracy may be lower"
    )

# ---------- Tab 3: Pilot Results ----------
with tab_pilot:
    st.markdown("### 30-question pilot")
    st.caption("Read from docs/pilot_run1.md (before) and docs/pilot_run2.md (after).")
    left, right = st.columns(2)
    for col, label, title in [(left, "run1", "Run 1: before changes"),
                              (right, "run2", "Run 2: after changes")]:
        with col:
            st.markdown(f"#### {title}")
            lines = pilot_summary(label)
            if not lines:
                st.info(f"No results yet. Run: python src\\run_pilot.py {label}")
                continue
            m = re.search(r"= (\d+)%", " ".join(lines))
            if m:
                st.metric("Accuracy", f"{m.group(1)}%", delta="target 85%", delta_color="off")
            for line in lines:
                st.write("• " + line)

    st.markdown("### Targets (from the project charter)")
    st.table({
        "Measure": ["Accuracy", "Average response time", "Citations on answers", "Refusal of out-of-scope questions"],
        "Target": ["85% or more", "under 2 seconds", "100%", "90% or more"],
    })