import webbrowser
import time
import random

def open_website(domain, service_url):
    url = service_url.format(domain)
    webbrowser.open(url)
    
services = {
    "Whois Lookup": "https://www.who.is/whois/{}",
    "Whoxy": "https://whoxy.com/{}",
    "Certificate": "https://crt.sh/?q={}",
    "Subdomains": "https://securitytrails.com/domain/{}",
    "Malware": "https://www.virustotal.com/gui/domain/{}",
    "builtwith": "https://builtwith.com/relationships/{}",
    "dnslytics": "https://dnslytics.com/domain/{}",
    "spyonweb": "https://spyonweb.com/{}",
    "archive": "https://web.archive.org/web/*/{}",
    "host": "https://host.io/{}"
}

with open("example.txt","r") as file:
    domains = [line.strip() for line in file]
    
for domain in domains: 
    for service_name, service_url in services.items():  
        open_website(domain, service_url)
        sleep_time = random.uniform(1, 5)
        time.sleep(sleep_time)