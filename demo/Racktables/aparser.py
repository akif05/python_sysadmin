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

for row in rows:
    print(row)
