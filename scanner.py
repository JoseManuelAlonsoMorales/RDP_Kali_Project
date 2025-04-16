import nmap
from datetime import datetime

def scan_network(network_range):
    nm = nmap.PortScanner()

    print(f"Scanning network: {network_range} for RDP (port 3389)...")
    try:
        nm.scan(hosts=network_range, arguments='-p 3389')
    except Exception as e:
        print(f"Error running nmap scan: {e}")
        return []

    # Create a unique log filename based on current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"nmap_log_{timestamp}.txt"

    active_hosts = []

    with open(filename, "w") as log:
        for host in nm.all_hosts():
            state = nm[host].state()
            log.write(f"\nHost: {host} - State: {state}\n")

            for proto in nm[host].all_protocols():
                for port in nm[host][proto]:
                    port_state = nm[host][proto][port]['state']
                    log.write(f"  Port {port} - {port_state}\n")

                    if port == 3389 and port_state == "open":
                        active_hosts.append(host)

    print(f"Scan complete. Log saved to {filename}")
    return active_hosts
