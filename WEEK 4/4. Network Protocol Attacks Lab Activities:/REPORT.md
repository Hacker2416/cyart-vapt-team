# Task 04: Network Protocol Attacks Lab (Report)

## 1. Aim / Objective
To perform network protocol attack simulations in a controlled lab environment and understand:
- NTLM credential capture using Responder
- Man-in-the-Middle (MitM) using ARP spoofing (Ettercap)
- Packet inspection and verification using Wireshark
- SMB relay workflow using Impacket ntlmrelayx

---

## 2. Tools Used
- **Responder**
- **Ettercap**
- **Wireshark**
- **Impacket (ntlmrelayx)**

---

## 3. Lab Environment & IP Details
| Device         | Role     | IP Address     |
|----------------|----------|----------------|
| Kali Linux     | Attacker | 192.168.75.135 |
| Windows 7      | Victim   | 192.168.75.136 |
| Router/Gateway | Gateway  | 192.168.75.254 |

---

## 4. Practical Work Performed

### 4.1 NTLM Hash Capture using Responder
**Purpose:** Capture NTLM authentication hashes sent by the victim system.

**Command Used:**
```bash
sudo responder -I eth0 -dwv
