# Task 06 – Capstone Project: Full VAPT Engagement (PTES)

## Overview
This task demonstrates a complete Vulnerability Assessment and Penetration Testing (VAPT) engagement following the PTES methodology. The target machine used for simulation was a vulnerable lab environment (Metasploitable2 / HTB-style VM) inside a controlled network.

## Tools Used
- Kali Linux
- Nmap
- Metasploit Framework
- Burp Suite
- OpenVAS / Greenbone Vulnerability Manager (GVM)

## Target Details
- Target IP: `192.168.75.131`
- Environment: Local VM Lab (Controlled network)

---

## PTES Phases Covered

### 1) Reconnaissance & Scanning
- Host discovery using ARP scan and Nmap
- Full service enumeration using Nmap scripts and version detection

### 2) Vulnerability Identification
- Identified vulnerable FTP service: `vsftpd 2.3.4`
- Verified exploit availability using `searchsploit`

### 3) Exploitation
- Exploited `vsftpd 2.3.4 backdoor` using Metasploit module:
  `exploit/unix/ftp/vsftpd_234_backdoor`
- Achieved successful shell access and verified root privileges

### 4) Web/API Testing (Burp Suite)
- Captured HTTP requests using Burp Proxy/Repeater
- Modified request headers (example: `X-Test: 123`) and validated responses

### 5) Vulnerability Scanning (OpenVAS)
- Performed vulnerability scan and documented findings
- Generated vulnerability list and severity results

