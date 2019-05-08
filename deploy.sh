#cloud-config

runcmd:
  - cd /root/synergy-ddos
  - screen -d -m -S dos bash -c 'source env/bin/activate; python ddos.py'