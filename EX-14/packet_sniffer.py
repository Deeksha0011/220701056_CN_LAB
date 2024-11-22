from scapy.all import sniff, conf, IP

def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        protocol = ip_layer.proto
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        # Determine the protocol
        protocol_name = ""
        if protocol == 1:
            protocol_name = "ICMP"
        elif protocol == 6:
            protocol_name = "TCP"
        elif protocol == 17:
            protocol_name = "UDP"
        else:
            protocol_name = "Unknown Protocol"

        # Print packet details
        print(f"Protocol: {protocol_name}")
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print("-" * 50)

def main():
    # Set Scapy to use Layer 3 socket to avoid the need for pcap libraries
    conf.L3socket = conf.L3socket  # Use L3socket instead of L2socket
    sniff(prn=packet_callback, filter="ip", store=0)

if __name__ == "__main__":
    main()