rows = []
for line in open("docs/pilot_run1.md", encoding="utf-8"):
    if line.startswith("| P"):
        c = [x.strip() for x in line.split("|")]
        try:
            rows.append((int(c[1][1:]), float(c[5]), c[7], c[2][:50]))
        except ValueError:
            pass

print("ID   score   result  question")
for n, s, r, q in rows:
    tag = "OUT-OF-SCOPE" if n > 25 else ""
    print(f"P{n:<3} {s:<7} {r:<7} {q} {tag}")

ans = [s for n, s, r, q in rows if n <= 25]
out = [s for n, s, r, q in rows if n > 25]
print("\nHighest score among answerable questions:", max(ans))
print("Lowest score among out-of-scope questions:", min(out))
if max(ans) < min(out):
    print("Suggested MAX_DISTANCE:", round((max(ans) + min(out)) / 2, 3))
else:
    print("The groups overlap. Try MAX_DISTANCE just above", round(max(ans), 3),
          "and check which answerable questions get refused.")