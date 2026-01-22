# Mobile Application Testing Lab - Report

## Tools
- MobSF
- Frida
- Drozer

---

## 1) Static Analysis (MobSF)
MobSF was executed using Docker and APK was uploaded for static analysis.  
The report showed multiple security issues such as insecure storage usage, debug configuration enabled, and sensitive data handling warnings.

### Result
Static analysis successfully detected insecure storage related issues.

---

## 2) Static Analysis Log (Enhanced Task)
| Test ID | Vulnerability     | Severity | Target App |
|---------|-------------------|----------|------------|
| 016     | Insecure Storage  | High     | diva.apk   |

---

## 3) Dynamic Testing (Frida)
Frida tools were installed and tested on Android Emulator.  
Processes were listed using Frida and the target application process was identified.  
Attempt was made to attach to the target app for dynamic instrumentation.

### Result
Frida was successfully installed and connected to emulator. Process listing and attach attempts were performed.

---

## 4) IPC Testing (Drozer)
Drozer is used to test Android IPC components such as exported activities, services, receivers, and content providers.

### Result
(Attach screenshot proof in GitHub)
