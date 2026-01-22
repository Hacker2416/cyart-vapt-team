## Executive Summary
This capstone task simulated a complete Vulnerability Assessment and Penetration Testing (VAPT) engagement using the PTES methodology in a controlled lab environment. 
The target machine was scanned and assessed to identify weaknesses in exposed services and web interfaces.
Initial reconnaissance and enumeration were performed using Nmap, which revealed multiple open ports and services. 
A vulnerable FTP service (vsftpd 2.3.4) was identified, which is known to contain a backdoor that can lead to remote code execution. 
Using Metasploit, the vulnerability was successfully exploited and root-level access was obtained, demonstrating the critical impact of outdated and misconfigured services.
Burp Suite was used to perform web/API testing by intercepting HTTP traffic and modifying request headers to validate request handling and response behavior.
OpenVAS was used to perform automated vulnerability scanning, generating severity-based findings and supporting the manual testing results.
The engagement concludes that the system is highly vulnerable due to insecure legacy services, weak hardening, and lack of patch management.

## Attack Timeline
The assessment began with host discovery and port scanning to identify active services. 
The vulnerable vsftpd service was detected and validated through exploit research. 
Exploitation was performed using Metasploit’s vsftpd backdoor module, resulting in successful unauthorized access. 
Evidence was collected using basic system commands (whoami, id, uname).
Web testing was conducted using Burp Suite by capturing and replaying requests.
OpenVAS scanning provided a vulnerability overview and severity ratings for reporting.

## Remediation Plan
Recommended actions include upgrading or replacing vsftpd 2.3.4 with a secure version, disabling FTP if not required, and enforcing firewall restrictions and network segmentation. 
Apply least privilege, remove unnecessary services, and ensure regular patching. For web/API security, implement strict input validation, authorization checks, secure configuration, and logging/monitoring. 
A rescan should be performed after patching to verify risk reduction.
