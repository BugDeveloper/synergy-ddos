#cloud-config

runcmd:
  - screen -d -m -S dos bash -c 'python3.7 /root/synergy-ddos/ddos.py'
  - mkdir /root/test