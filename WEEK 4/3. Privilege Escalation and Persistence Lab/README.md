# Task 03 – Privilege Escalation and Persistence Lab

## Objective
The objective of this task is to perform privilege escalation on a vulnerable Linux VM, gain root access, and establish persistence. This includes enumeration using LinPEAS, identifying SUID misconfigurations, exploiting them to get a root shell, and configuring persistence using a cron job.

---

## Tools Used
- Metasploit Framework
- LinPEAS
- Linux Commands (find, id, whoami, cron)

---

## Target Details
- **Attacker Machine:** Kali Linux  
- **Attacker IP:** `192.168.75.135`  
- **Target VM:** VulnHub / Vulnerable Linux VM  
- **Target IP:** `192.168.75.131`

---

## Work Performed 
### 1) Initial Access
- Gained shell access using Metasploit (vsftpd backdoor)
- Verified root access using `whoami` and `id`

### 2) Enumeration
- Performed system enumeration using LinPEAS
- Identified privilege escalation vectors (SUID binaries)

### 3) Privilege Escalation
- Discovered SUID enabled binary: `/usr/bin/nmap`
- Used Nmap interactive mode to spawn root shell

### 4) Persistence
- Created a cron job in `/etc/cron.d/` for persistence
- Verified persistence by checking output written to `/tmp/persist.txt`


