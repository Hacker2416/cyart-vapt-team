# Burp Suite Testing Notes

## Activity
- Captured HTTP GET request to target web server
- Sent request to Repeater
- Modified request headers for validation testing

## Test Performed
Added custom header:
X-Test: 123

## Result
Server responded with 200 OK and returned HTML content successfully.
