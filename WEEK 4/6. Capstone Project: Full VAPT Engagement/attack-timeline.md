# Attack Timeline (PTES)

| Timestamp (IST)           | Target IP        | Vulnerability / Action                  | PTES Phase                   |
|--------------------------|------------------|------------------------------------------|------------------------------|
| 2026-01-22 15:55:00      | 192.168.75.131   | Host discovery (ARP scan / Nmap -sn)     | Reconnaissance               |
| 2026-01-22 15:59:00      | 192.168.75.131   | Full port scan + service enumeration     | Scanning                     |
| 2026-01-22 16:02:00      | 192.168.75.131   | vsftpd 2.3.4 detected on FTP (21/tcp)    | Vulnerability Identification |
| 2026-01-22 16:05:25      | 192.168.75.131   | Exploited VSFTPD backdoor (RCE)          | Exploitation                 |
| 2026-01-22 16:06:00      | 192.168.75.131   | Verified root access (whoami/id/uname)   | Post-Exploitation            |
| 2026-01-22 16:12:00      | 192.168.75.131   | HTTP confirmed open (80/tcp)             | Enumeration                  |
| 2026-01-22 16:14:00      | 192.168.75.131   | Burp Suite request capture + header test | Web/API Testing              |
| 2026-01-22 16:30:00      | 192.168.75.131   | OpenVAS scan completed                   | Validation                   |
| 2026-01-22 16:40:00      | 192.168.75.131   | Remediation plan documented              | Reporting                    |
