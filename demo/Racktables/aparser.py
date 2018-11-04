import requests
import lxml.html as lh
import pandas as pd
import re
import sys
import sys
import json
import os.path
from bs4 import BeautifulSoup 

with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'lxml')

table = soup.find("table",{"class":"cooltable"})
rows = table.find_all('tr')

i = 0
for row in rows:
    i += 1
    if i>400 and i<402:
        print(row)
