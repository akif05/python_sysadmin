import requests
import lxml.html as lh
import pandas as pd
import re
import sys
import sys
import json
import os.path
from bs4 import BeautifulSoup 

with open("object.html") as fp:
    soup = BeautifulSoup(fp, 'lxml')

## get <div class="portlet">
## inside the div is the table we need. Get the table
## This talbe contains all the objects element in racktables
div = soup.find("div", {"class":"portlet"})
table = div.find("table")

results = {}
nl = '\n'
rows = table.find_all("tr")

i = 0
for row in rows:
    i += 1
    # th         :   td
    # Common name:	zeta
    aux_td = row.find_all('td')
    aux_th = row.find_all('th')
    
    print(f'AAAAA: {aux_th}: {aux_td}{nl}')
    results[aux_th] = aux_td
print (results) 


# name.append(re.findall(r'<strong>(.*?)</strong>', str(row.find_all('strong'))))
# object_id.append(re.findall(r'object_id=([0-9]*)">', str(row))) 


