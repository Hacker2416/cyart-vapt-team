# Task 04 - Network Protocol Attacks Lab

## Objective
Perform Network Protocol Attacks to understand Man-in-the-Middle (MitM) techniques and credential capture using common tools.

## Tools Used
- Responder
- Ettercap
- Wireshark
- Impacket (ntlmrelayx)

## Lab Setup (IP Mapping)
| System         |Role      | IP Address     |
|----------------|----------|----------------|
| Kali Linux     | Attacker | 192.168.75.135 |
| Windows 7      | Victim   | 192.168.75.136 |
| Router/Gateway | Gateway  | 192.168.75.254 |

---

## Task Checklist (As per Practical)
✅ Capture NTLM hashes (Responder)  
✅ Spoof DNS / MitM (Ettercap)  
✅ Analyze traffic (Wireshark)  
✅ SMB Relay attempt using ntlmrelayx (Enhanced Task)

---

## 1) NTLM Hash Capture using Responder

### Command Used
```bash
sudo responder -I eth0 -dwv
