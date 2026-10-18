from qa import ask

# (question, expected answer in short, expected source or "none")
TESTS = [
    ("How do I reset my password?", "Click Forgot password; link expires in 30 min", "login_and_sso.md"),
    ("Which plans support SSO?", "Business and Enterprise", "login_and_sso.md"),
    ("When do backups run?", "Every night at 2 AM UTC", "backups.md"),
    ("How long are backups kept on Enterprise?", "90 days", "backups.md"),
    ("How much is the Business plan?", "$79 per month", "pricing_and_plans.md"),
    ("Is there a free trial?", "Yes, 14 days, no card", "pricing_and_plans.md"),
    ("What is the API limit on Starter?", "60 requests per minute", "api_limits.md"),
    ("What error appears when I exceed the limit?", "429", "api_limits.md"),
    ("Who is the CEO of Acme Cloud?", "I don't know", "none"),
    ("Does Acme Cloud have a mobile app?", "I don't know", "none"),
]

lines = ["# Test Scenario Log\n",
         "Sample data: 4 markdown files written for this project.\n",
         "| ID | Question | Expected | Answer | Sources | Seconds | Pass/Fail |",
         "|---|---|---|---|---|---|---|"]

for i, (q, expected, src) in enumerate(TESTS, 1):
    r = ask(q)
    answer = r["answer"].replace("\n", " ").replace("|", "/")
    lines.append(f"| T{i} | {q} | {expected} | {answer} | "
                 f"{', '.join(r['sources'])} | {r['seconds']} | (fill in) |")
    print(f"T{i} done ({r['seconds']}s)")
from pathlib import Path
out_path = Path(__file__).resolve().parent.parent / "docs" / "test_scenario_log.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("Saved", out_path)