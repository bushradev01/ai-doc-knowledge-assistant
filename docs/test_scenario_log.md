# Test Scenario Log


| ID  | Question                         | Result | Why (Example)                                      |
|-----|----------------------------------|--------|----------------------------------------------------|
| T1  | How do I reset my password?      | Pass   | Mentioned "Forgot password"                       |
| T2  | Which plans support SSO?         | Pass   | Said Business and Enterprise                       |
| T3  | When do backups run?             | Pass   | Said 2 AM UTC                                      |
| T4  | Backup retention on Enterprise?  | Fail   | Said 30 days instead of 90                         |
| T5  | How much is the Business plan?   | Pass   | Said $79                                           |
| T6  | Is there a free trial?           | Pass   | 14 days, no card                                   |
| T7  | API limit on Starter?            | Pass   | 60 per minute                                      |
| T8  | Error when over the limit?       | Pass   | 429                                                |
| T9  | Who is the CEO?                  | Fail   | Invented a name instead of saying "I don't know"   |
| T10 | Does it have a mobile app?       | Pass   | Said "I don't know"                                |

## Summary
- Model: qwen2.5:0.5b, local via Ollama (embeddings: nomic-embed-text)
- Tests run: 10
- Passed: 8
- Failed: 2 (T4, T9)
- Average response time: 1.07 seconds (first question 2.8 sec while the model loaded)
- Problems found: small model ignored the "I don't know" rule once and
  mixed up the Enterprise and Business retention; sources list all
  retrieved files, not only the ones used
- Planned fix for Week 3: stricter prompt, retrieve fewer chunks, show only
  the best-matching source, try a larger model