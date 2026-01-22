# Attack Log

## Attack ID: 015
**Technique:** SMB Relay / NTLM Capture  
**Attacker IP:** 192.168.75.135  
**Victim IP:** 192.168.75.136  
**Gateway IP:** 192.168.75.254  

### Steps
1. Started Responder on Kali to capture NTLM authentication requests.
2. Started ntlmrelayx SMB relay server using a target file.
3. Triggered authentication from Windows victim using UNC path.
4. Captured NTLMv2 hashes successfully.

### Status
Success

### Outcome
NTLMv2 hashes captured successfully from the victim system.
