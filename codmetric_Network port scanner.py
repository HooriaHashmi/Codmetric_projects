import socket
from concurrent.futures import ThreadPoolExecutor

# Common ports and their services (can be expanded)
COMMON_PORTS = {
    20: "FTP (Data)",
    21: "FTP (Control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
}

def scan_port(ip: str, port: int, timeout: float = 1.0) -> tuple:
    """
    Scan a single port on the target IP address.
    
    Args:
        ip: Target IP address
        port: Port number to scan
        timeout: Connection timeout in seconds
        
    Returns:
        Tuple of (port, status, service) where status is True if open
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((ip, port))
            service = COMMON_PORTS.get(port, "Unknown service")
            return (port, result == 0, service)
    except socket.error:
        return (port, False, "Error scanning")

def port_scanner(ip: str, start_port: int = 1, end_port: int = 1024, max_threads: int = 100) -> None:
    """
    Scan a range of ports on the target IP address.
    
    Args:
        ip: Target IP address
        start_port: First port in range (default: 1)
        end_port: Last port in range (default: 1024)
        max_threads: Maximum concurrent threads (default: 100)
    """
    print(f"\nScanning {ip} (ports {start_port}-{end_port})...")
    print("WARNING: Only scan networks you are authorized to scan!\n")
    
    open_ports = []
    
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        
        for future in futures:
            port, is_open, service = future.result()
            if is_open:
                open_ports.append((port, service))
                print(f"[+] Port {port} is open - {service}")
    
    if not open_ports:
        print("No open ports found in the specified range.")
    else:
        print("\nScan complete. Open ports:")
        for port, service in sorted(open_ports):
            print(f"  - Port {port}: {service}")

def get_target_info() -> tuple:
    """
    Get target IP and port range from user input with validation.
    
    Returns:
        Tuple of (ip, start_port, end_port)
    """
    print("Simple Network Port Scanner")
    print("--------------------------")
    print("IMPORTANT: Only scan systems you have explicit permission to scan!\n")
    
    while True:
        ip = input("Enter target IP address (e.g., 127.0.0.1): ")
        try:
            socket.inet_aton(ip)  # Validate IP address
            break
        except socket.error:
            print("Invalid IP address format. Please try again.")
    
    while True:
        try:
            start_port = int(input("Enter starting port (1-65535): "))
            end_port = int(input("Enter ending port (1-65535): "))
            
            if 1 <= start_port <= end_port <= 65535:
                break
            print("Invalid port range. Ensure 1 ≤ start ≤ end ≤ 65535")
        except ValueError:
            print("Please enter valid integers for port numbers.")
    
    return (ip, start_port, end_port)

if __name__ == "__main__":
    target_ip, start_p, end_p = get_target_info()
    port_scanner(target_ip, start_p, end_p)