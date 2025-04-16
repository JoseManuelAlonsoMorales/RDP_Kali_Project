#!/usr/bin/env python3
import subprocess
import sys

def connect_rdp(ip, user, password):
    print(f"Conectando a {ip} con el usuario {user}…")
    try:
        subprocess.run(
            ["xfreerdp3", f"/v:{ip}", f"/u:{user}", f"/p:{password}", "/cert:ignore"],
            check=True
        )
        print("Conexión RDP finalizada.")
    except subprocess.CalledProcessError as e:
        print(f"Error al conectar vía RDP: {e}")
    except FileNotFoundError:
        print("El comando 'xfreerdp3' no está instalado. Ejecuta:\n  sudo apt install freerdp3-x11")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Uso: {sys.argv[0]} <IP> <usuario> <contraseña>")
        sys.exit(1)
    _, ip, user, password = sys.argv
    connect_rdp(ip, user, password)
