import requests
import lxml.html as lh
import pandas as pd
import re
import sys
import sys
import json
import os.path
from bs4 import BeautifulSoup 

## Read an html file to variable soup.
with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'lxml')

## Get Table that is in class 'cooltable'
## This talbe contains all the objects element in racktables
table = soup.find("table",{"class":"cooltable"})

## Get all elements from the talbe that are rows by class
rows = table.find_all("tr", {"class": ["row_odd", "row_even"]})

name = []

## Create list of hostnames extracting name between strong html tags!
for row in rows:
    name.append(re.findall(r'<strong>(.*?)</strong>', str(row.find_all('strong'))))
    #name.append(str(row.find_all('strong')))

for n in name:
    print (n)
