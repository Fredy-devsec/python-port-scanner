import socket
import time

def banner():
       print("""
╔══════════════════════════════════════════════╗
║                                              ║
║                 SCAN FREDY                   ║
║             PYTHON PORT SCANNER              ║
║                                              ║
║              Developed by Fredy              ║
║                                              ║
╚══════════════════════════════════════════════╝
""")


def scan_port(target, port):
       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       sock.settimeout(0.5)

       result = sock.connect_ex((target, port))
       sock.close()

       return result == 0

def get_service(port):
       try:
              return socket.getservbyport(port, "tcp")
       except OSError:
              return "unknown"

banner()

target = input("Target IP: ")

print(f"\nScanning {target}...")
print("-"*50)

start_time = time.time()

for port in range(1,1025):
       
       if scan_port(target, port):
              
            service = get_service(port)

            print(f"[+] {port}/TCP     OPEN       {service.upper()}")

end_time = time.time()

print("-"*50)
print(f"Scan completed in {end_time - start_time:.2f} seconds.")
print("Scan perfomed by Fredy") 