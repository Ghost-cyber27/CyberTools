import socket
import requests

def check_open_ports(host, ports):
    open_ports = []
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set a timeout for the connection
            if s.connect_ex((host, port)) == 0:
                open_ports.append(port)
    return open_ports

def check_server_version(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            server = response.headers.get('Server', 'Unknown')
            return server
        else:
            return f"Error: Received status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

def main():
    host = input("Enter the host (IP or domain): ")
    ports = [80, 443, 21, 22, 25, 3306]  # Common ports to check

    print(f"Checking open ports on {host}...")
    open_ports = check_open_ports(host, ports)
    
    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")

    url = f"http://{host}"
    print(f"Checking server version at {url}...")
    server_version = check_server_version(url)
    print(f"Server version: {server_version}")

if __name__ == "__main__":
    main()
