# Burp Suite Manual Testing

## Steps
1. Configure browser proxy to Burp Suite.
2. Intercept DVWA requests.
3. Observe cookies and session tokens.
4. Modify parameters to test input handling.
5. Remove cookie and resend request.

## Result
Without valid session cookie, DVWA redirected to login page (HTTP 302), confirming session-based authentication enforcement.
