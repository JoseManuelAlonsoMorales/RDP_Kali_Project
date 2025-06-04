#!/usr/bin/env python3
import nmap
import sys
from datetime import datetime

def scan_network(network_range):
    nm = nmap.PortScanner()

    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] Escaneando red: {network_range} para conexiones RDP (puerto 3389)...\n")
    try:
        nm.scan(hosts=network_range, arguments='-p 3389')
    except Exception as e:
        print(f"[!] Error al ejecutar el escaneo con nmap: {e}")
        return []

    active_hosts = []

    for host in nm.all_hosts():
        state = nm[host].state()
        print(f"Host: {host} - Estado: {state}")

        for proto in nm[host].all_protocols():
            for port in nm[host][proto]:
                port_state = nm[host][proto][port]['state']
                print(f"  Puerto {port}/{proto} - Estado: {port_state}")

                if port == 3389 and port_state == "open":
                    print(f"  [✔] RDP ABIERTO en {host}\n")
                    active_hosts.append(host)

    return active_hosts

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: ./scanner.py <rango_de_red>")
        print("Ejemplo: ./scanner.py 192.168.1.0/24")
        sys.exit(1)

    network_range = sys.argv[1]
    hosts = scan_network(network_range)

    if hosts:
        print("Resumen: Hosts con RDP abierto encontrados:")
        for h in hosts:
            print(f"  - {h}")
    else:
        print("No se encontraron hosts con RDP abierto.")
