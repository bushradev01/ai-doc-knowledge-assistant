# Pilot Run: run2

| ID | Question | Answer | Sources | Best score | Seconds | Auto result |
|---|---|---|---|---|---|---|
| P1 | How do I reset my password? | To reset your password, click "Forgot password" on the login page. | login_and_sso.md > Password Reset | 0.416 | 3.03 | Pass |
| P2 | How long does the password reset link last? | The password reset link lasts for 30 minutes. | login_and_sso.md > Password Reset | 0.522 | 0.36 | Pass |
| P3 | Which plans support SSO? | The plans that support SSO are the Business and Enterprise plans. | login_and_sso.md > Single Sign-On | 0.529 | 0.6 | Pass |
| P4 | Which SSO protocols are supported? | SSO is supported through SAML 2.0 and Google Workspace login. | login_and_sso.md > Single Sign-On | 0.557 | 0.52 | Pass |
| P5 | Can I log in with Google? | Yes, you can log in with Google. | login_and_sso.md > Single Sign-On | 0.756 | 0.47 | Pass |
| P6 | When do backups run? | Backups run every night at 2 AM UTC. | backups.md > Schedule | 0.486 | 0.58 | Pass |
| P7 | How long are backups kept on the Enterprise plan? | 90 days | backups.md > Schedule | 0.382 | 0.44 | Pass |
| P8 | How long are backups kept on the Business plan? | 30 days | backups.md > Schedule | 0.373 | 0.16 | Pass |
| P9 | How do I restore a backup? | To restore a backup, follow these steps:  1. Go to Settings > Backups. 2. Choose a date. 3. Click Restore. 4. Wait for about 10 to 15 minutes. | backups.md > Restoring a Backup | 0.389 | 0.98 | Pass |
| P10 | How long does a restore take? | A restore takes about 10 to 15 minutes. | backups.md > Restoring a Backup | 0.368 | 0.58 | Pass |
| P11 | How much is the Business plan? | The Business plan costs $79 per month. | pricing_and_plans.md > Plans | 0.645 | 0.74 | Pass |
| P12 | How much is the Starter plan? | The Starter plan costs $19 per month. | pricing_and_plans.md > Plans | 0.599 | 0.78 | Pass |
| P13 | How long is the free trial? | The free trial is 14 days. | pricing_and_plans.md > Free Trial | 0.55 | 1.54 | Pass |
| P14 | Do I need a credit card for the free trial? | No, you do not need a credit card for the free trial. | pricing_and_plans.md > Free Trial | 0.479 | 1.47 | Pass |
| P15 | What is the API rate limit on the Starter plan? | The API rate limit on the Starter plan is 60 API requests per minute. | api_limits.md > Rate Limits | 0.315 | 1.98 | Pass |
| P16 | What is the API rate limit on the Business plan? | The API rate limit on the Business plan is 600 requests per minute. | api_limits.md > Rate Limits | 0.305 | 0.78 | Pass |
| P17 | Which error code appears when I exceed the API limit? | I don't know based on the provided documents. | none | 0.41 | 1.3 | Fail |
| P18 | How is data encrypted at rest? | Data is encrypted at rest with AES-256 and in transit with TLS 1.3. | security.md > Encryption | 0.529 | 1.41 | Pass |
| P19 | How is data encrypted in transit? | Data is encrypted in transit with TLS 1.3. | security.md > Encryption | 0.503 | 1.1 | Pass |
| P20 | Is two-factor authentication available? | Yes, two-factor authentication is available. | security.md > Two-Factor Authentication | 0.192 | 1.33 | Pass |
| P21 | How long are audit logs kept? | Audit logs are kept for 180 days on the Enterprise plan only. | security.md > Audit Logs | 0.329 | 1.58 | Pass |
| P22 | What is the support email address? | The support email address is support@acmecloud.example. | support.md > Contact | 0.456 | 1.33 | Pass |
| P23 | How fast does Business support reply? | Business support replies within 8 business hours. | support.md > Response Times | 0.479 | 1.35 | Pass |
| P24 | Does Enterprise have phone support? | Yes, Enterprise has phone support. | support.md > Response Times | 0.505 | 0.84 | Pass |
| P25 | How fast is the response for critical Enterprise issues? | Based on the provided context, the response times for critical Enterprise issues are within 8 business hours. | support.md > Response Times | 0.478 | 1.46 | Fail |
| P26 | Who is the CEO of Acme Cloud? | I don't know based on the provided documents. | none | 0.651 | 1.18 | Pass |
| P27 | Does Acme Cloud have a mobile app? | No, Acme Cloud does not have a mobile app. | support.md > Contact | 0.618 | 1.2 | Fail |
| P28 | Where are the Acme data centers located? | The Acme data centers are located in different locations. | support.md > Contact | 0.677 | 0.58 | Fail |
| P29 | Is there a student discount? | I don't know based on the provided documents. | none | 0.902 | 0.07 | Pass |
| P30 | How do I cancel my account? | I don't know based on the provided documents. | none | 0.799 | 0.08 | Pass |

## Summary
- Questions: 30
- Passed (automatic keyword check): 26 / 30 = 87%
- Average response time: 0.99 sec
- Slowest response: 3.03 sec
- Median response time: 0.98 sec
- Answerable questions with a citation: 24 / 25