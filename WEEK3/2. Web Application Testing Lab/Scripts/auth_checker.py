import requests

url = "http://192.168.75.131/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit"

r = requests.get(url, allow_redirects=False)

print("Status Code:", r.status_code)
print("Redirect Location:", r.headers.get("Location"))
