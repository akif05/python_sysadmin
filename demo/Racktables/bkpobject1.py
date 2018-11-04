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

## Implement this as function to which pass th object id and 
## Retrive data from url:, 
#  https://racktables-001.sl5.misp.co.uk/racktables/index.php?page=object&tab=default&object_id=179


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
common_name = object_dict.get('Common_name')
asset_tag = object_dict.get('Asset_tag')
fqdn = object_dict.get('FQDN')
line = "=" * 50

if "Shared cPanel" in explisit_tags:
    print(line)
    print(f' FQDN: {fqdn}{nl} Common name: {common_name}{nl} \
Explisit tags: {explisit_tags}{nl} Tag:{asset_tag}')
    print(line)

