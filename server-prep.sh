#!/bin/bash
# Run this as user root from the working copy folder

# Set hostname and reboot first!

apt-get update -y
apt-get upgrade -y

apt-get install mc etckeeper python-is-python3 authbind certbot

pip install -r requirements.txt

mkdir -p /root/bin
mkdir -p /root/log
cp renew-cert.sh /root/bint/renew-cert.sh
chmod +x
cp root-crontab.txt /root/bin/crontab
crontab /root/bin/crontab

if ! [ -d /home/plugin ]; then
  adduser plugin
fi

for PORT in 80 443; do
  FP=/etc/authbind/byport/$PORT
  touch $FP
  chown plugin:plugin $FP
  chmod +x $FP
done

# Create SSH cert, authorized_keys
# Copy files to server
# Append profile.sh to ~/.profile of user plugin
# Copy or create certs (./etc/letsencrypt)
# Run renew-cert.sh once to copy certs into /home/plugin/cert
# Load plugin user's crontab
