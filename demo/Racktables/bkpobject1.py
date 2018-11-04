import requests
import lxml.html as lh
import pandas as pd
import re
import sys
import sys
import json
import os.path
import pprint
from bs4 import BeautifulSoup 


with open("/Users/akifyusein/object.html") as fp:
    soup = BeautifulSoup(fp, 'lxml')

## get <div class="portlet">
## inside the div is the table we need. Get the table
## This talbe contains all the objects element in racktables
div = soup.find("div", {"class":"portlet"})
table = div.find("table")

results = {}
nl = '\n'
rows = table.find_all("tr")
aux_th_list = []
aux_td_list = []
i = 0
for row in rows:
    i += 1
    # th         :   td
    # Common name:	zeta
    aux_th = row.th
    aux_td = row.td
   
    # Strip out the : that are on th tag string! 
    aux_th_key = str(aux_th.text.strip().strip(":").replace(" ", "_"))
    aux_td_val = str(aux_td)

    # Create dictionary
    results[str(aux_th_key)] = aux_td_val

for key, value in results.items():
    if key == "Common_name":
        print(key)

