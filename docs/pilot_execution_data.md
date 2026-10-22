# Pilot Execution Data (Week 3)

**Date:** 23 October 2026
**Setup:** Streamlit app on one laptop, FAISS index of 6 sample files,
local Ollama (nomic-embed-text + qwen2.5:0.5b), MAX_DISTANCE=0.76,
1 citation per answer.

## 1. Automated test: 30 questions (25 answerable, 5 out-of-scope)
Full logs: [Run 1](pilot_run1.md) and [Run 2](pilot_run2.md)

| Measure | Target | Run 1 (before) | Run 2 (after) |
|---|---|---|---|
| Accuracy | 85%+ | 83% (25/30) | 87% (26/30) |
| Average response time | under 2 sec | (copy from pilot_run1.md) | about 0.99 sec |
| Slowest response | | 3.36 sec (model loading) | 3.03 sec (model loading) |
| Out-of-scope refused | 90%+ | 2 of 5 (40%) | 3 of 5 (60%) |
| Still failing | | P17, P25, P27, P28, P29 | P17, P25, P27, P28 |

## 2. Changes made between runs
| Change | Reason (from data) |
|---|---|
| Sources cited 2 to 1 | The password question showed an irrelevant backups.md source |
| MAX_DISTANCE=0.76 | Run 1 gave invented answers to out-of-scope questions. The cutoff was set just above the highest score of a valid question (0.756) so no valid question is blocked |

## 3. Live test: 9 new questions
These questions were not used to tune the cutoff. They were typed in the app
by three testers (Khadija, Amna, Sara), three questions each.

| Tester | Question | App answer (short) | Expected | Result | Best score |
|---|---|---|---|---|---|
| Khadija | Does Acme Cloud support SAML? | Yes, SAML | Yes (SAML 2.0) | Pass | 0.436 |
| Khadija | How long are audit logs kept? | 180 days, Enterprise only | 180 days, Enterprise | Pass | 0.329 |
| Khadija | Does Acme Cloud have a Linux desktop app? | "No, it does not" | I don't know | Fail | 0.690 |
| Amna | What encryption is used in transit? | TLS 1.3 | TLS 1.3 | Pass | 0.468 |
| Amna | How much is the Enterprise plan? | $79 per month | Custom pricing | Fail | 0.678 |
| Amna | What is the refund policy? | I don't know | I don't know | Pass | 1.064 |
| Sara | When does the password reset link expire? | After 30 minutes | 30 minutes | Pass | 0.496 |
| Sara | How fast does Business support reply? | Within 8 business hours | 8 business hours | Pass | 0.479 |
| Sara | Who founded Acme Cloud? | "Alibaba Cloud" (invented) | I don't know | Fail | 0.700 |

| Live measure | Result |
|---|---|
| Correct overall | 6 of 9 (67%), target 85% not met |
| Answerable questions correct | 5 of 6 |
| Out-of-scope questions refused | 1 of 3 |
| Average response time | about 0.38 sec |
| Answers with a citation (answerable) | 6 of 6 |

## 4. User ratings
(Choose ONE option and delete the other.)

**Option A: ratings collected**

| Tester | Trust in sources (1-5) | Ease of use (1-5) | One improvement (their words) |
|---|---|---|---|
| Khadija | | | |
| Amna | | | |
| Sara | | | |

**Option B: ratings not collected**
User ratings (trust, ease of use) were not collected because the testers were
unavailable. They are planned for Week 4 before the final report.

## 5. Findings
- **What worked:** answers are fast (under 1 second on average), citations
  point to the right file and section, and in-scope questions were mostly
  correct (5 of 6 live, 25 of 25 answerable pilot questions except two).
- **What failed:** the small model gives invented or wrong answers when a
  question is close to the documents but not covered. Examples: the Enterprise
  price ($79 instead of custom pricing), a founder name, and "no Linux app".
- **Most serious problem:** a wrong answer shown with a citation looks
  trustworthy. Showing a source does not prove the answer is correct.
- **Cutoff limit:** out-of-scope questions scored 0.69 to 0.70, while one
  valid pilot question scored 0.756. One distance cutoff cannot separate
  them. The 87% pilot accuracy was tuned on the same 30 questions, so the
  67% live result is the fairer estimate of real accuracy.
- **Refusal quality:** 60% in the pilot, 33% live (4 of 8 combined = 50%).
  Target 90% is not met.
- **Week 1 personas:** the simulated personas predicted that users distrust
  confident answers without evidence. The live test confirms that risk: the
  confident wrong answer was the main failure.

## 6. Plan for Week 4
1. Lower the cutoff toward 0.65 and re-run both the 30-question and 9-question
   tests. Check how many valid questions it wrongly refuses.
2. Make the prompt stricter: answer only when the context states the exact
   fact, otherwise reply with the "I don't know" sentence.
3. Try a larger model (llama3.2:1b or llama3.2) and compare accuracy and speed.
4. Add a short "answers may be wrong, check the source" note in the app.
5. Collect real user ratings.