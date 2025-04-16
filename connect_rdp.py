#!/usr/bin/env python3
import subprocess
import sys

def connect_rdp(ip, user, password):
    print(f"Connecting to {ip} as user '{user}'...")

    try:
        # Build and execute the xfreerdp3 command
        subprocess.run(
            ["xfreerdp3", f"/v:{ip}", f"/u:{user}", f"/p:{password}", "/cert:ignore"],
            check=True
        )
        print("RDP session ended.")

    except subprocess.CalledProcessError as e:
        print(f"Error during RDP connection: {e}")

    except FileNotFoundError:
        print("The 'xfreerdp3' command is not installed. You can install it using:\n  sudo apt install freerdp3-x11")

if __name__ == "__main__":
    # Ensure the user provides exactly 3 arguments (IP, username, password)
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <IP> <username> <password>")
        sys.exit(1)

    # Unpack arguments and call the connect_rdp function
    _, ip, user, password = sys.argv
    connect_rdp(ip, user, password)
