import socket

def scan_ports(host, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            sock.connect((host, port))
            open_ports.append(port)
        except (socket.timeout, socket.error):
            pass
        finally:
            sock.close()

    return open_ports

def get_service_name(port):
    well_known_ports = {
        20: "FTP - Data",
        21: "FTP - Control",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        465: "SMTPS",
        587: "SMTP (Submission)",
        993: "IMAPS",
        995: "POP3S",
        3306: "MySQL",
        3389: "RDP (Remote Desktop Protocol)",
        # Adicione mais portas e serviços conforme necessário
    }

    return well_known_ports.get(port, "Unknown Service")

def main():
    host = input("Enter the target host: ")
    port_range = input("Enter the port range (e.g., 1-100): ")

    try:
        start_port, end_port = map(int, port_range.split('-'))
    except ValueError:
        print("Invalid port range. Please use format: start-end")
        return

    open_ports = scan_ports(host, start_port, end_port)

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            service_name = get_service_name(port)
            print(f"{port}: {service_name}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()