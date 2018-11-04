import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml.html as lh
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
url = "https://racktables-001.sl5.misp.co.uk/racktables/index.php?page=object&tab=default&object_id=179"

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

## Print out the the whole file. Can be redirected to fiel from command line
print(r.text)
