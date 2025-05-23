# Instructions to set up the RDP client environment on Kali Linux

1. **Update packages and system:**

   `sudo apt update && sudo apt upgrade -y`

2. **Install required tools:**

   `sudo apt install -y freerdp3-x11 hydra`

3. **Reset current network configurations:**

   `sudo ip addr flush dev eth0`

4. **Assign a new IP address:**

   `sudo ip addr add 192.168.100.101/24 dev eth0`

5. **Enable the network interface:**

   `sudo ip link set eth0 up`

6. **Connect to the RDP server:**

   `xfreerdp3 /u:kali /p:kali /v:192.168.100.100 /cert:ignore`

7. **Log out from the RDP session:**

   `pkill xfreerdp3`
