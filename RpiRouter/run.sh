#!/bin/bash

echo "Enabling IP forwarding..."
echo 1 > /proc/sys/net/ipv4/ip_forward

echo "Setting up iptables rules..."
iptables -t nat -A POSTROUTING -o enu1 -j MASQUERADE
iptables -A FORWARD -i enu1 -o end0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i end0 -o enu1 -j ACCEPT

echo "Router setup complete."
tail -f /dev/null  # Keep the container running
