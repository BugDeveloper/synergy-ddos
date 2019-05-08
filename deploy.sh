#cloud-config

runcmd:
  - screen -d -m -S dos bash -c 'python3.7 ddos.py'
  - mkdir test