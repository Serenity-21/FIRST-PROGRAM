#!/usr/bin/env python3
import sys
import dns.resolver

# Check for arguments
if len(sys.argv) < 2:
    print("Usage: dnsseeker <domain>")
    sys.exit(1)

target_domain = sys.argv[1]
records_type = ['A', 'AAAA', 'CNAME', 'MX', 'TXT']

# Use Google + Cloudflare DNS servers for consistency
resolver = dns.resolver.Resolver()
resolver.nameservers = ["8.8.8.8", "1.1.1.1"]
resolver.timeout = 2
resolver.lifetime = 2

for record in records_type:
    try:
        answer = resolver.resolve(target_domain, record)
        print(f"\n{record} records for {target_domain}:")

        if record == "MX":
            for data in answer:
                print(f"Priority: {data.preference}, Mail Server: {data.exchange}")
        elif record == "TXT":
            for data in answer:
                # TXT may contain multiple strings
                print(" ".join(s.decode() for s in data.strings))
        else:
            for data in answer:
                print(data)

    except dns.resolver.NoAnswer:
        print(f"No {record} record found")
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist")
        break
    except Exception as e:
        print(f"Error fetching {record}: {e}")

