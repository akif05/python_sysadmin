#! /Users/akifyusein/.virtualenvs/demo/bin/python3 -W ignore
import whois, re, requests
from ipwhois import IPWhois
from pprint import pprint
import sys
# Install 'pip install whois'

# Check if argument is given from command line if not exit
if len(sys.argv) > 1:
    filename = sys.argv[1]
    print (filename)
else:
    print (f'Usage: {sys.argv[0]} filename')
    sys.exit()

domains_ip = []
domains_name = []
with open(filename) as f:
    content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    # Extract the site name from the line which is first
    for line in content:
        x = line.split(" : ")
        domains_name.append(x[0])
        if len(x) == 2:
            domains_ip.append(x[1])
        else:
            domains_ip.append("NONE")

# Use i to track list in domains_name list and access them by index
i = 0
for ip_addr in domains_ip:
    if ip_addr == "NONE":
        i += 1
        print ('"%s" -- "%s"' % (name, "NO-IP-ADDRESS"))
        continue

    ip_addr = ip_addr.strip('\"')
    obj = IPWhois(ip_addr)
    res = obj.lookup_whois()
    name = res["nets"][0]['name']
    description = res["nets"][0]['description']
    if not name:
        name = description
    print ('"%s", "%s", "%s"' % (ip_addr, domains_name[i], name))

    # print ('"%s" -- "%s" : "%s" -- "%s"' % (name, description, ip_addr, domains_name[i]))
    i += 1
