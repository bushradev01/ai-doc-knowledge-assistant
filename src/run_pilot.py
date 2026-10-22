import sys
from pathlib import Path
from qa import ask

# (question, any of these words counts as correct; ["IDK"] = should refuse)
TESTS = [
    ("How do I reset my password?", ["forgot password"]),
    ("How long does the password reset link last?", ["30 minutes"]),
    ("Which plans support SSO?", ["business", "enterprise"]),
    ("Which SSO protocols are supported?", ["saml"]),
    ("Can I log in with Google?", ["google"]),
    ("When do backups run?", ["2 am"]),
    ("How long are backups kept on the Enterprise plan?", ["90"]),
    ("How long are backups kept on the Business plan?", ["30 days"]),
    ("How do I restore a backup?", ["settings"]),
    ("How long does a restore take?", ["10"]),
    ("How much is the Business plan?", ["79"]),
    ("How much is the Starter plan?", ["19"]),
    ("How long is the free trial?", ["14"]),
    ("Do I need a credit card for the free trial?", ["no credit card", "not required", "don't need", "do not need"]),
    ("What is the API rate limit on the Starter plan?", ["60"]),
    ("What is the API rate limit on the Business plan?", ["600"]),
    ("Which error code appears when I exceed the API limit?", ["429"]),
    ("How is data encrypted at rest?", ["aes"]),
    ("How is data encrypted in transit?", ["tls"]),
    ("Is two-factor authentication available?", ["all plans", "yes"]),
    ("How long are audit logs kept?", ["180"]),
    ("What is the support email address?", ["support@acmecloud.example"]),
    ("How fast does Business support reply?", ["8"]),
    ("Does Enterprise have phone support?", ["24/7", "phone"]),
    ("How fast is the response for critical Enterprise issues?", ["1 hour", "1-hour", "one hour"]),
    ("Who is the CEO of Acme Cloud?", ["IDK"]),
    ("Does Acme Cloud have a mobile app?", ["IDK"]),
    ("Where are the Acme data centers located?", ["IDK"]),
    ("Is there a student discount?", ["IDK"]),
    ("How do I cancel my account?", ["IDK"]),
]

label = sys.argv[1] if len(sys.argv) > 1 else "run1"
rows, times = [], []
passed = cited = answerable = 0

for i, (q, keys) in enumerate(TESTS, 1):
    r = ask(q)
    ans = r["answer"].replace("\n", " ").replace("|", "/")
    low = ans.lower()
    if keys == ["IDK"]:
        ok = "don't know" in low
    else:
        ok = any(k in low for k in keys)
        answerable += 1
        if r["sources"]:
            cited += 1
    passed += ok
    times.append(r["seconds"])
    rows.append(f"| P{i} | {q} | {ans} | {'; '.join(r['sources']) or 'none'} | "
                f"{r['scores'][0] if r['scores'] else ''} | {r['seconds']} | {'Pass' if ok else 'Fail'} |")
    print(f"P{i} {'Pass' if ok else 'Fail'} ({r['seconds']}s)")

times_sorted = sorted(times)
summary = [
    f"# Pilot Run: {label}\n",
    "| ID | Question | Answer | Sources | Best score | Seconds | Auto result |",
    "|---|---|---|---|---|---|---|",
    *rows,
    "\n## Summary",
    f"- Questions: {len(TESTS)}",
    f"- Passed (automatic keyword check): {passed} / {len(TESTS)} = {round(100*passed/len(TESTS))}%",
    f"- Average response time: {round(sum(times)/len(times), 2)} sec",
    f"- Slowest response: {max(times)} sec",
    f"- Median response time: {times_sorted[len(times)//2]} sec",
    f"- Answerable questions with a citation: {cited} / {answerable}",
]
out = Path(__file__).resolve().parent.parent / "docs" / f"pilot_{label}.md"
out.write_text("\n".join(summary), encoding="utf-8")
print("Saved", out)