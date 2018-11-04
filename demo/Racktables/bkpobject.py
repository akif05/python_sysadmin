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

# Rad from html file or use requests tor read from url, check or_new_parser.py
with open("/Users/akifyusein/object.html") as fp:
    soup = BeautifulSoup(fp, 'lxml')

## get <div class="portlet">
## inside the div is the table we need. Get the table
## This talbe contains all the objects element in racktables
div = soup.find("div", {"class":"portlet"})

# read the content between <table> and </talbe> tags in variable table
table = div.find("table")

# Read all table row in variable rows
rows = table.find_all("tr")

key_list = []
value_list = []
object_dict = {}
nl = '\n'

for row in rows:
   
    # Strip out the : that are on th tag string! 
    key_list.append(str(row.th.text.strip().strip(":").replace(" ", "_")))
    value_list.append(str(row.td.text.strip()))

# Create dictinary from elements read from each row in table
object_dict = dict(zip(key_list, value_list))

explisit_tags=object_dict.get('Explicit_tags')
#print (object_dict.get('Common_name'))
#print (object_dict.get('Explicit_tags'))

if "Shared cPanel" in explisit_tags:
    print(explisit_tags)

#for key, value in object_dict.items():
    #if key == "Common_name":
    # print(f'{key} -- {value}')
#    print(key)

