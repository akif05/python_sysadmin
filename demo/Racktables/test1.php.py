import requests
import lxml.html as lh
import pandas as pd
import bs4 as bs
# import urllib2
import re
import sys
import unicodedata
import sys
import json
import configparser
import os.path

config_file = sys.argv[1]
url = sys.argv[2]
if config_file == "" or url == "":
    print ("Provied config file and url!")
    sys.exit()


config = configparser.ConfigParser()
try:
    config.read(config_file)
except:
    print(f"Reading file {config_file} problem")
    sys.exit(2)

password = config.get("myvars", "passwd");
username = config.get("myvars", "username");

try:
    r = requests.get(url, auth=(username, password))
except:
    print(f"Error accessing {url}")
    sys.exit(3)

if r.status_code != 200:
    print(f'Can not get to the URL {url}')
    sys.exit(4)

html = r.content
soup = bs.BeautifulSoup(html, 'lxml')
table = soup.find("table",{"class":"cooltable"})
# print (table.text)
rows = table.find_all('tr')
for row in rows:
    print(row)