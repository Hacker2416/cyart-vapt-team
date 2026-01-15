A capstone VAPT cycle was performed on a vulnerable lab machine (Metasploitable2) to simulate a real penetration testing workflow.
The assessment included reconnaissance, vulnerability scanning, exploitation, and reporting. 
Initial intelligence gathering was performed using Nmap to enumerate open ports and service versions.
Multiple services were discovered including FTP, SSH, HTTP, SMB, and MySQL, indicating a large attack surface.
A vulnerability scan was conducted using OpenVAS/Greenbone, which highlighted several high and critical issues related to outdated and insecure services. 
Based on the scan and service enumeration, exploitation was attempted against the FTP service. 
he target was running a vulnerable VSFTPD version and was successfully exploited using Metasploit (exploit/unix/ftp/vsftpd_234_backdoor). 
The exploit resulted in a command shell session and root-level access was confirmed using system commands such as whoami, id, and uname.
This confirms that an attacker can fully compromise the target system, execute arbitrary commands, and potentially access sensitive data or pivot to other machines. 
Recommended remediation includes patching or removing vulnerable services, restricting exposed ports using firewall rules, applying least privilege, and performing regular vulnerability scanning. 
After fixes are applied, a rescan should be conducted to verify the remediation effectiveness.
