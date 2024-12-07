import socket
import whois
import requests

def get_ip_address(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None

def get_dns_records(domain):
    try:
        records = socket.gethostbyname_ex(domain)
        return records
    except socket.gaierror:
        return None

def get_whois_info(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return str(e)

def get_http_headers(url):
    try:
        response = requests.get(url)
        return response.headers
    except requests.exceptions.RequestException as e:
        return str(e)

def main():
    domain = input("Enter the domain to footprint (e.g., example.com): ")

    print("\nGathering information...\n")

    # Get IP Address
    ip_address = get_ip_address(domain)
    if ip_address:
        print(f"IP Address: {ip_address}")
    else:
        print("Could not resolve IP address.")

    # Get DNS Records
    dns_records = get_dns_records(domain)
    if dns_records:
        print(f"DNS Records: {dns_records}")
    else:
        print("Could not retrieve DNS records.")

    # Get WHOIS Information
    whois_info = get_whois_info(domain)
    print(f"\nWHOIS Information:\n{whois_info}")

    # Get HTTP Headers
    url = f"http://{domain}"
    http_headers = get_http_headers(url)
    print(f"\nHTTP Headers:\n{http_headers}")

if __name__ == "__main__":
    main()
