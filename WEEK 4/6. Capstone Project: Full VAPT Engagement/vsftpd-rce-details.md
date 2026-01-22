# VSFTPD 2.3.4 Backdoor – RCE

## Vulnerability
The FTP service running vsftpd 2.3.4 contains a known backdoor that can allow attackers to execute commands remotely.

## Attack Vector
- Remote attacker connects to FTP service
- Exploit triggers backdoor listener
- Attacker gains unauthorized shell access

## Evidence Collected
- Metasploit session opened successfully
- Root access confirmed using:
  - whoami
  - id
  - uname -a

## Business Impact
- Unauthorized access to system resources
- Data leakage risk
- Potential lateral movement inside network
