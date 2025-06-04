#!/usr/bin/env python3
import nmap
import sys
from datetime import datetime

def scan_network(network_range):
    nm = nmap.PortScanner()

    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Scanning network: {network_range} for RDP connections (port 3389)...\n")
    try:
        nm.scan(hosts=network_range, arguments='-p 3389')
    except Exception as e:
        print(f"[!] Error running nmap scan: {e}")
        return []

    active_hosts = []

    for host in nm.all_hosts():
        state = nm[host].state()
        print(f"Host: {host} - State: {state}")

        for proto in nm[host].all_protocols():
            for port in nm[host][proto]:
                port_state = nm[host][proto][port]['state']
                print(f"  Port {port}/{proto} - State: {port_state}")

                if port == 3389 and port_state == "open":
                    print(f"  [✔] RDP OPEN on {host}\n")
                    active_hosts.append(host)

    return active_hosts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./scanner.py <network_range>")
        print("Example: ./scanner.py 192.168.1.0/24")
        sys.exit(1)

    network_range = sys.argv[1]
    hosts = scan_network(network_range)

    if hosts:
        print("Summary: Hosts with open RDP found:")
        for h in hosts:
            print(f"  - {h}")
    else:
        print("No hosts with open RDP found.")
