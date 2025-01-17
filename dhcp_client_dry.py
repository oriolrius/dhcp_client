#!/usr/bin/env python3
from scapy.all import *
from scapy.layers.dhcp import *
from scapy.layers.inet import UDP, IP
from scapy.layers.l2 import Ether

def send_dhcp_discover(interface):
    # Create a DHCP Discover packet
    dhcp_discover = (
        Ether(dst='ff:ff:ff:ff:ff:ff') /
        IP(src='0.0.0.0', dst='255.255.255.255') /
        UDP(sport=68, dport=67) /
        BOOTP(chaddr=RandMAC()) /
        DHCP(options=[("message-type", "discover"), "end"])
    )
    sendp(dhcp_discover, iface=interface)
    print("Sent DHCP Discover packet")

def handle_dhcp_packet(packet):
    if DHCP in packet and packet[DHCP].options[0][1] == 2:  # Offer
        print("Received DHCP Offer:")
        packet.show()

    elif DHCP in packet and packet[DHCP].options[0][1] == 5:  # Ack
        print("Received DHCP Ack:")
        packet.show()

def main():
    interface = "eth0"  # Replace with your interface name
    send_dhcp_discover(interface)
    
    # Sniff DHCP packets on the specified interface
    print("Sniffing for DHCP packets...")
    sniff(iface=interface, filter="udp and (port 67 or 68)", prn=handle_dhcp_packet, timeout=30)

if __name__ == "__main__":
    main()
