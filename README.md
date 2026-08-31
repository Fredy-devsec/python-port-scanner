# 🔐 ScanFredy — Python Port Scanner

A simple TCP port scanning project developed in Python for **educational purposes and cybersecurity learning**.

This repository contains two versions of a basic port scanner, developed step by step to understand how network connections, TCP ports, sockets, and basic service identification work.

> ⚠️ **Educational Project:** This tool was created for learning purposes. Only scan systems, devices, networks, or virtual machines that you own or have explicit permission to test.

---

## 📖 About the Project

**ScanFredy** is a small Python-based project created while studying **Information Technology and Cybersecurity**.

The main goal of this project is not to create a professional replacement for tools such as Nmap, but rather to understand the fundamental concepts behind a simple TCP port scanner by building one from scratch.

The project currently contains two scanners:

* 🟢 **Scanner V1** — Basic TCP port scanner
* 🔵 **Scanner V2** — Improved scanner with a custom interface and basic service identification

This project is part of my learning journey in Python, networking, and cybersecurity.

---

# 🟢 Scanner V1 — Basic Port Scanner

The first version is intentionally simple.

It asks for a target IP address and checks TCP ports from **1 to 1024**.

### Example

```text
Enter target IP: 127.0.0.1

[+] Port 22 is OPEN
[+] Port 80 is OPEN
[+] Port 443 is OPEN
```

The scanner uses Python's built-in `socket` module to attempt TCP connections.

### 🎯 What I learned from V1

While developing the first version, I practiced:

* Python variables
* `input()`
* `for` loops
* `range()`
* conditional statements
* TCP sockets
* IPv4 addresses
* ports
* connection timeouts
* basic error handling

---

# 🔵 Scanner V2 — ScanFred

The second version improves the first scanner by introducing a more organized structure and a simple terminal interface.

It includes:

* 🖥️ Custom ScanFred banner
* 🎯 Target IP input
* 🔎 TCP port scanning
* 📡 TCP protocol identification
* 🧩 Basic service identification
* ⏱️ Scan execution time
* 🧱 Functions for better code organization

### Example

```text
╔══════════════════════════════════════════════╗
║                                              ║
║                 SCAN FREDY                   ║
║             PYTHON PORT SCANNER              ║
║                                              ║
║              Developed by Fredy              ║
║                                              ║
╚══════════════════════════════════════════════╝

Target IP: 127.0.0.1

Scanning 127.0.0.1...
--------------------------------------------------

[+] 22/TCP    OPEN    SSH
[+] 80/TCP    OPEN    HTTP
[+] 443/TCP   OPEN    HTTPS

--------------------------------------------------
Scan completed in 1.42 seconds.
Scan performed by Fredy.
```

---

# 🧠 How Does It Work?

The scanner uses Python's built-in `socket` module.

At a high level, the process is:

```text
User
 │
 │ enters target IP
 ▼
ScanFred
 │
 │ creates TCP socket
 ▼
Target IP + Port
 │
 │ attempts TCP connection
 ▼
Connection result
 │
 ├── Connection accepted → OPEN
 │
 └── Connection refused/failed → CLOSED or unavailable
 │
 ▼
Display result
```

The scanner does not attempt to exploit vulnerabilities or gain unauthorized access.

Its purpose is to understand whether a TCP connection can be established to a particular port.

---

# 🔧 Technologies Used

### Programming Language

* Python 3

### Python Modules

The project uses mainly Python's standard library:

```python
import socket
import time
```

No external Python packages are required for the current versions.

---

# 📦 Requirements

You only need:

* Python 3.x
* A terminal
* A computer or virtual machine where you have permission to perform the scan

You can verify your Python installation with:

```bash
python --version
```

or:

```bash
python3 --version
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Fredy-devsec/scanfred.git
```

Enter the project directory:

```bash
cd scanfred
```

You can then run either scanner.

---

# ▶️ Usage

## Scanner V1

Run:

```bash
python scanner_v1.py
```

The program will ask:

```text
Enter target IP:
```

For example:

```text
127.0.0.1
```

The scanner will then test TCP ports from:

```text
1 → 1024
```

---

## Scanner V2

Run:

```bash
python scanner_v2.py
```

Enter the target IP when requested:

```text
Target IP: 127.0.0.1
```

The scanner will test the configured port range and display open TCP ports.

---

# 🧪 Safe Testing

For learning purposes, I recommend starting with your own computer.

### Localhost

```text
127.0.0.1
```

`127.0.0.1` refers to the local machine.

You can also use a virtual machine or cybersecurity training environment where you have explicit authorization to perform network testing.

For example:

```text
Your computer
      │
      ├── Python
      │
      └── ScanFred
              │
              ▼
        Your test environment
```

---

# ⚠️ Ethical and Legal Use

Port scanning can be a legitimate cybersecurity technique, but scanning systems without permission may violate laws, regulations, network policies, or terms of service.

**Only use ScanFred against:**

* systems you own;
* your own computer;
* your own virtual machines;
* intentionally vulnerable laboratory environments;
* systems for which you have explicit authorization to perform security testing.

I created this project strictly as part of my cybersecurity and programming studies.

The purpose is to **learn how networking and security tools work**, not to perform unauthorized access or attacks.

---

# 🔍 Important Limitations

ScanFred is a **learning project**, not a professional network scanner.

It currently has several limitations.

### 1. TCP only

The current versions focus on TCP connections.

They do not perform UDP scanning.

### 2. Limited port range

The initial scanner checks ports:

```text
1–1024
```

### 3. Basic service identification

Scanner V2 uses the operating system's known service mappings to associate common ports with service names.

For example:

```text
22 → SSH
80 → HTTP
443 → HTTPS
```

This does **not** prove that the service running on the port is actually that protocol.

For example:

```text
443/TCP OPEN HTTPS
```

means that TCP port 443 is open and that port 443 is conventionally associated with HTTPS.

It does not perform full service detection.

### 4. No vulnerability exploitation

ScanFred does not attempt to exploit discovered services.

### 5. No advanced reconnaissance

The project does not currently provide features such as:

* OS fingerprinting
* advanced service detection
* vulnerability detection
* stealth scanning
* UDP scanning
* packet crafting
* exploit modules

These features are outside the scope of the current learning project.

---

# 📚 What This Project Taught Me

Building this project helped me understand concepts that are difficult to fully appreciate by only using existing tools.

Some of the concepts I practiced include:

### Python

* Variables
* Functions
* Loops
* Conditions
* Exception handling
* Modules
* String formatting

### Networking

* IPv4
* TCP
* Ports
* Client connections
* Sockets
* Timeouts

### Cybersecurity

* Network reconnaissance
* Port enumeration
* Basic service identification
* Security testing methodology
* Ethical and authorized security testing

---

# 🧩 Project Structure

The repository currently contains the two learning stages:

```text
scanfred/
│
├── scanner_v1.py
├── scanner_v2.py
└── README.md
```

### `scanner_v1.py`

The original and simpler implementation.

Its purpose is to demonstrate the basic concept of TCP port scanning.

### `scanner_v2.py`

An improved version with:

* custom interface;
* functions;
* service identification;
* scan timing;
* cleaner output.

---

# 📈 Future Improvements

This project is intentionally being developed step by step.

Possible future improvements include:

* [ ] Command-line arguments
* [ ] Custom port ranges
* [ ] Better error handling
* [ ] Improved terminal interface
* [ ] Scan progress indicator
* [ ] Export scan results to a file
* [ ] Basic banner grabbing in authorized lab environments
* [ ] Improved service detection
* [ ] Multithreaded scanning
* [ ] Configuration file
* [ ] Unit tests
* [ ] Better project documentation

The goal is to implement these features gradually while understanding the underlying concepts rather than simply copying existing tools.

---

# 🧠 Learning Philosophy

This project represents one step in my cybersecurity learning journey.

I'm still learning and improving my knowledge of Python, networking, Linux, and cybersecurity.

Instead of trying to build a complex security tool immediately, I prefer to start with simple projects and gradually increase their complexity.

My goal is to understand **why** something works, not just **how** to make it work.

> **Learn → Build → Test → Understand → Improve**

---

# 🚀 Project Roadmap

### Version 0.1

Basic TCP port scanner.

### Version 0.2

Improved interface and basic service identification.

### Version 0.3

Command-line arguments.

### Version 0.4

Custom port selection.

### Version 0.5

Improved service detection.

### Version 0.6+

Additional features, testing, optimization, and documentation.

---

# 👨‍💻 About Me

I'm a **4th-year Information Technology student in Italy**, currently developing my knowledge in programming and cybersecurity.

I'm particularly interested in:

* 🔐 Cybersecurity
* 🕶️ Ethical Hacking
* 🛡️ Defensive & Offensive Security
* 🐍 Python
* 🌐 Networking
* 🤖 Artificial Intelligence
* 🔬 Security Research
* 🧩 Reverse Engineering

I'm still at the beginning of my journey, and this repository is one of the projects I'm using to learn by building.

---

<h3 align="center">⚡ Think like a hacker. Build like an engineer. ⚡</h3>

<p align="center">
  <i>Built for learning. Improved through practice.</i>
</p>
