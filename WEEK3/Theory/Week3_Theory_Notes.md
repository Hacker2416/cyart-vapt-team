# Week 3 Theory Notes

## 1) Advanced Vulnerability Exploitation
### Exploit Chains
Exploit chaining means using multiple vulnerabilities together to achieve a final goal like admin access or remote code execution.  
Example: XSS → session hijacking → admin panel access → RCE exploit.

### Exploit Customization
Public PoCs often require changes like target IP, URL paths, parameters, payload settings, or headers to work in real environments.

### Obfuscation Techniques
Obfuscation helps bypass filters/WAFs:
- URL encoding
- HTML encoding
- Base64
- case variations
- polymorphic payloads

---

## 2) Web Application Penetration Testing
### OWASP Top 10 Focus
- SQL Injection
- XSS
- Broken Authentication
- Security Misconfiguration
- Insecure Design

### Testing Techniques
Manual testing: Burp Suite interception, parameter tampering, cookie manipulation  
Automated testing: sqlmap, OWASP ZAP scanning

### Secure Coding Mitigations
- Input validation
- Output encoding
- Prepared statements
- secure session management

---

## 3) Reporting & Stakeholder Communication
### Report Structure
- Executive Summary
- Technical Findings
- Evidence
- Risk rating / CVSS
- Remediation steps

### Audience Tailoring
Managers: business impact summary  
Developers: technical steps to reproduce + fix

### KPIs
- total vulnerabilities found
- exploit success rate
- time-to-remediate
