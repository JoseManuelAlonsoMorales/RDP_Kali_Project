#!/bin/bash

# Script para preparar el entorno del cliente RDP en Kali Linux

echo "[+] Actualizando el sistema..."
sudo apt update && sudo apt upgrade -y

echo "[+] Instalando xfreerdp3 y hydra..."
sudo apt install -y xfreerdp3-x11 hydra

echo "[+] Configurando la red (IP fija)..."
sudo ip addr flush dev eth0
sudo ip addr add 192.168.10.2/24 dev eth0
sudo ip link set eth0 up

echo "[+] Probando conexión RDP al servidor..."
xfreerdp3 /u:kali /p:kali /v:192.168.10.1 /cert:ignore

echo "[+] Cerrando sesión RDP..."
pkill xfreerdp3

echo "[✔] Cliente preparado."
