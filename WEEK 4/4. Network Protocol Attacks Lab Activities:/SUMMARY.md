In this task, network protocol attacks were simulated using Responder, Ettercap, and Wireshark. 
Responder was used to capture NTLMv2 hashes from the Windows victim machine. Ettercap was used to perform ARP spoofing to establish a Man-in-the-Middle position between the victim and the gateway. 
Wireshark confirmed ARP poisoning and captured the redirected traffic. An SMB relay setup was configured using Impacket ntlmrelayx to demonstrate the relay workflow and authentication trigger process.
