#!/usr/bin/env python3
import threading
from scapy.all import *
from scapy.layers.dhcp import BOOTP, DHCP
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
    if DHCP in packet:
        dhcp_message_type = packet[DHCP].options[0][1]
        if dhcp_message_type == 2:  # Offer
            print("Received DHCP Offer:")
            packet.show()
        elif dhcp_message_type == 5:  # Ack
            print("Received DHCP Ack:")
            packet.show()

def main():
    interface = "eth0"  # Replace with your interface name

    # Start sniffing in a separate thread
    sniff_thread = threading.Thread(target=sniff, kwargs={
        'iface': interface,
        'filter': "udp and (port 67 or 68)",
        'prn': handle_dhcp_packet,
        'timeout': 30
    })
    sniff_thread.start()

    # Send DHCP Discover packet
    send_dhcp_discover(interface)

    # Wait for the sniffing thread to finish
    sniff_thread.join()

if __name__ == "__main__":
    main()
