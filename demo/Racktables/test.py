import requests
import lxml.html as lh
import pandas as pd
from bs4 import BeautifulSoup
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

doc = lh.fromstring(r.content)
#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')
col = []
i = 0

# Since out first row is the header, data is stored on the second row onwards
for j in range(1, len(tr_elements)):
    # T is our j'th row
    T = tr_elements[j]

    # If row is not of size 10, the //tr data is not from our table
    if len(T) != 4:
        break

    # i is the index of our column
    i = 0

    # Iterate through each element of the row
    for t in T.iterchildren():
        data = t.text_content()
        # Check if row is empty
        if i > 0:
            # Convert any numerical value to integers
            try:
                data = int(data)
            except:
                pass
        # Append the data to the empty list of the i'th column
        col[i][1].append(data)
        # Increment i for the next column
        i += 1

#[len(T) for T in tr_elements[1:12]]
#for t in tr_elements[0]:
#    i += 1
#    name = t.text_content()
#    print (f'{i}: {name}')
#    col.append((name, []))

