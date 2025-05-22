# Instructions to set up the RDP server environment on Kali Linux

1. **Update packages and system:**

   `sudo apt update && sudo apt upgrade -y`

2. **Install xrdp (RDP server):**

   `sudo apt install xrdp`

3. **Install XFCE4 desktop environment:**

   `sudo apt install xfce4`

4. **Configure XFCE4 as the default session for xrdp:**

   `echo "startxfce4" > ~/.xsession`

5. **Enable and start the xrdp service:**

   `sudo systemctl enable xrdp`  
   `sudo systemctl start xrdp`

6. **Reset current network configurations:**

   `sudo ip addr flush dev eth0`

7. **Assign a new IP address:**

   `sudo ip addr add 192.168.100.100/24 dev eth0`

8. **Enable the network interface:**

   `sudo ip link set eth0 up`
