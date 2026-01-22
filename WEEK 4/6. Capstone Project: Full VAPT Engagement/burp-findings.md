# Burp Findings

## Observation
The server accepts requests with custom headers and responds normally.

## Risk (General)
If APIs exist, weak validation and lack of authentication/authorization can lead to:
- Unauthorized access
- Data exposure
- Parameter tampering

## Recommendation
- Apply strict validation and sanitization
- Enforce authentication & authorization checks
- Use secure headers and logging
