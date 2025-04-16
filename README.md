---
title: RDP_Kali_Project
description: Implementation and testing of Remote Desktop Protocol (RDP) on Kali Linux for remote administration, cybersecurity, and pentesting purposes.
author: José Manuel Alonso Morales and Jesús Alexis MArtínez Arenas
version: 1.0
date: 2025-04-16
tags: [RDP, Kali Linux, cybersecurity, pentesting, Python, VirtualBox]
---

# RDP_Kali_Project


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

- client/ # Scripts and configuration for the RDP client VM
- server/ # Scripts and setup for the RDP server VM
- connect_rdp.py # Connects to RDP server using xfreerdp3
- scanner.py # Scans the internal network for active RDP sessions
- brute_force.py # Performs a brute-force attack on RDP using hydra
- session_logger.py # Logs active RDP session IPs and timestamps to a text file
- main.py # Central script that runs scanning, attack, connection an session loger logic
- users.txt # List of potential usernames
- passwords.txt # List of potential passwords
RDP_Kali_Project/ │ ├── client/ # Scripts and configuration for the RDP client VM │ └── install_xfreerdp.sh # (Optional) Script to install xfreerdp3 │ ├── server/ # Scripts and setup for the RDP server VM │ └── install_xrdp_xfce.sh # (Optional) Script to install xrdp and xfce4 │ ├── scripts/ # Python automation and attack scripts │ ├── connect_rdp.py # Connects to RDP server using xfreerdp3 │ ├── scanner.py # Scans the internal network for active RDP sessions │ ├── brute_force.py # Performs a brute-force attack on RDP using hydra │ ├── session_logger.py # Logs active RDP session IPs and timestamps to a text file │ └── main.py # Central script that runs scanning, attack, and connection logic │ ├── dictionaries/ # Username and password dictionaries │ ├── users.txt # List of potential usernames │ └── passwords.txt # List of potential passwords │ ├── docs/ # Documentation and technical notes │ └── setup_guide.md # Step-by-step setup and usage instructions │ 
