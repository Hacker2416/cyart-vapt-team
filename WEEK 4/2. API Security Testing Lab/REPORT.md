# Week 04 - Task 02 Report
## API Security Testing Lab (Burp Suite, Postman, sqlmap)

---

## 1. Objective
To perform API security testing on a lab environment using Burp Suite, Postman, and sqlmap. The objective includes identifying potential API vulnerabilities, attempting OWASP API Top 10 checks such as BOLA and GraphQL injection, and documenting all results with evidence.

---

## 2. Tools Used
1. Burp Suite (Repeater / manual testing)
2. Postman (API request testing + GraphQL fuzzing)
3. sqlmap (SQL injection exploitation/validation)
4. Gobuster (endpoint enumeration)

---

## 3. Target Details
- Target IP: `192.168.75.131`
- Base URL: `http://192.168.75.131`
- Application Environment: DVWA (Damn Vulnerable Web Application)

---

## 4. Methodology Followed
The testing process was performed in the following steps:
1. Endpoint Enumeration (Gobuster)
2. Manual Parameter Testing (Burp Suite)
3. SQL Injection Validation (sqlmap)
4. API Request Testing (Postman)
5. BOLA Endpoint Testing Attempt (`/api/users`)
6. GraphQL Fuzzing Attempt (`/graphql`)
7. Documentation and Evidence Collection

---

## 5. Endpoint Enumeration (Gobuster)
### Command Used
```bash
gobuster dir -u http://192.168.75.131/ -w /usr/share/wordlists/dirb/common.txt -t 30
