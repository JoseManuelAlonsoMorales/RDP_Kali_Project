# RDP_Kali_Project

## Project Overview

RDP_Kali_Project is a project that explores Remote Desktop Protocol (RDP) communications between two Kali Linux virtual machines using VirtualBox. It combines RDP configuration, internal networking, and Python scripting to simulate real situations involving remote access, connection monitoring, and brute-force authentication testing.

## Technologies Used

- Virtual Box
- Kali Linux
- Python

## Virtual Environment Setup

The project uses two Kali Linux virtual machines running on VirtualBox, connected by an internal network:

- Client VM: Configured with `xfreerdp3`, a RDP client.
- Server VM: Configured with `xrdp` as the RDP server and `xfce4` as the desktop environment.

## Project Objectives

This project aims to:

1. Establish an RDP connection between the client and server VMs.
2. Automate the RDP connection using Python scripts.
3. Verify active RDP sessions.
4. Execute a brute-force attack using dictionaries of usernames and passwords.
5. Develop a script that monitors active RDP sessions and logs the connection time and IP address of the connecting machine to a txt file.

## Project Structure

- `client.md`  
  Scripts and configuration for the RDP client VM.

- `server.md`  
  Scripts and setup for the RDP server VM.

- `connect_rdp.py`  
  Connects to the RDP server using `xfreerdp3`.

- `scanner.py`  
  Scans the internal network for active RDP sessions.

- `brute_force.py`  
  Performs a brute-force attack on RDP using `hydra`.

- `session_logger.py`  
  Logs active RDP session IPs and timestamps to a text file.

- `main.py`  
  Central script that runs scanning, attack, connection, and session logger logic.

- `users.txt`  
  List of potential usernames for brute-force testing.

- `passwords.txt`  
  List of potential passwords for brute-force testing.

---

## Disclaimer

This project is intended for **educational purposes only**.

---

## Authors

José Manuel Alonso Morales and Jesús Alexis Martínez Arenas  
April 2025
