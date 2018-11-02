import requests
import sys
import json
import configparser
import os.path
conf_filename = "/Users/akifyusein/.my_a_pass"

print(conf_filename)
if not os.path.isfile(conf_filename):
    print(f'File: {conf_filename} does not exist')
    sys.exit(1)
# https://stackoverflow.com/questions/924700/best-way-to-retrieve-variable-values-from-a-text-file-python-json
# read configuration from file
# file format

#$ cat ~/.my_a_pass
# [myvars]
# username: my_username
# passwd: my_password
if len(sys.argv) != 2:
    print("Please provide Url to proceede")
    sys.exit(1)

# Check if url exitst

url = sys.argv[1]

config = configparser.ConfigParser()
try:
    config.read(conf_filename)
except:
    print(f"Reading file {conf_filename} problem")
    sys.exit(2)

password = config.get("myvars", "passwd")
username = config.get("myvars", "username")

try:
    r = requests.get(url, auth=(username, password))
except:
    print(f"Error accessing {url}")
    sys.exit(3)

if r.status_code != 200:
    print(f'Can not get to the URL {url}')
    sys.exit(4)

print(r.text)

## F string examples
# print(f'Username: {username}')
# print(f'passwd: {password}')

## Thise are working examples!!!
# with open('new_whit_whit.html', 'w') as f:
#    print(r.text, file=f)

# sys.stdout=open('new_wiht_open.html', 'w')
# print(r.text)
# sys.stdout.close()

