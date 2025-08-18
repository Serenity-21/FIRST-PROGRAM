#!/usr/bin/env python3
import requests
import threading
import os
import sys

# check if domain is provided
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <target_domain>")
    sys.exit(1)

target_domain = sys.argv[1]

# load subdomains
if os.path.exists('subdomains.txt'):
    with open('subdomains.txt') as f:
        subdomains = f.read().splitlines()
else:
    subdomains = ['www', 'mail', 'ftp', 'admin', 'test', 'dev', 'api']

discovered_subdomains = []
lock = threading.Lock()

def check_subdomain(subdomain):
    for scheme in ["http", "https"]:
        url = f"{scheme}://{subdomain}.{target_domain}"
        try:
            response = requests.get(url, timeout=3, headers={"User-Agent": "Mozilla/5.0"})
            if response.status_code < 400:
                print('[+] Discovered subdomain:', url)
                with lock:
                    discovered_subdomains.append(url)
        except Exception:
            pass  # suppress noisy errors

threads = []
for subdomain in subdomains:
    thread = threading.Thread(target=check_subdomain, args=(subdomain,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

with open('discovered_subdomains.txt', 'w') as f:
    for subdomain in discovered_subdomains:
        print(subdomain, file=f)

print("\n[+] Results saved to discovered_subdomains.txt")

