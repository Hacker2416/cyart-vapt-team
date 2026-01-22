# Week 04 - Task 02: API Security Testing Lab
## Test Setup Log (Required)

| Test ID | Vulnerability     | Severity  | Target Endpoint | Tool Used | Result / Observation                                                       |
|--------|--------------------|------------|----------------|-----------|----------------------------------------------------------------------------|
| 008    | BOLA               | Critical   | /api/users     | Postman   | Endpoint not found (404) – REST API not exposed in DVWA environment        |
| 009    | GraphQL Injection  | High       | /graphql       | Postman   | Endpoint not found (404) – GraphQL endpoint not deployed/enabled on target |
