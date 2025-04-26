from scapy.all import sniff, IP, TCP, UDP, Raw

def process_packet(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        src_ip = packet[IP].src  # Source IP address
        dst_ip = packet[IP].dst  # Destination IP address
        protocol = packet[IP].proto  # Protocol number
        
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol}")
        
        # Check for transport layers (TCP or UDP)
        if TCP in packet or UDP in packet:
            transport_layer = TCP if TCP in packet else UDP
            src_port = packet[transport_layer].sport  # Source port
            dst_port = packet[transport_layer].dport  # Destination port
            print(f"Source Port: {src_port}")
            print(f"Destination Port: {dst_port}")
        
        # Check for application layer data (payload)
        if Raw in packet:
            payload = packet[Raw].load  # Payload data
            print(f"Payload: {payload}")
        else:
            print("Payload: No data")
        
        print("-" * 50)

def start_sniffer(interface=None):
    """
    Start sniffing packets on the specified network interface.
    If no interface is provided, it defaults to the system's primary interface.
    """
    print("Starting packet sniffer...")
    sniff(iface=interface, prn=process_packet, store=False)

if __name__ == "__main__":
    # Replace 'eth0' with the appropriate network interface (e.g., wlan0 for Wi-Fi)
    start_sniffer(interface="eth0")
