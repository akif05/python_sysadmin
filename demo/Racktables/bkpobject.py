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
#with open("/Users/akifyusein/object.html") as fp:
def get_shared_cpanel_server(beauty_soap, explisit_tag):

    key_list = []
    value_list = []
    object_dict = {}
    nl = '\n'
    
    div = beauty_soap.find("div", {"class":"portlet"})
    table = div.find("table")
    rows = table.find_all("tr")
    
    for row in rows:
        # Strip out the : that are on th tag string! 
        key_list.append(str(row.th.text.strip().strip(":").replace(" ", "_")))
        value_list.append(str(row.td.text.strip()))
    # Create dictinary from elements read from each row in table
    object_dict = dict(zip(key_list, value_list))
    
    explisit_tags=object_dict.get('Explicit_tags')
    
    if explisit_tag in explisit_tags:
        return object_dict

def print_obj_dict(object_dict):

    nl = '\n'
    line = "=" * 50
    explisit_tags=object_dict.get('Explicit_tags')
    common_name = object_dict.get('Common_name')
    asset_tag = object_dict.get('Asset_tag')
    fqdn = object_dict.get('FQDN')
   
    s = """FQDN: %s\nCommon name: %s\nExplisit tags: %s\nTag: %s """ \
     % ( fqdn, common_name, explisit_tags, asset_tag)

    print(line)
    print(s)
    print(line)

html_file = "/Users/akifyusein/object.html"
def main():

    ## Read from html file or from requests.text to create soup of all objects
    ## Generate a list of all objects id if are not pdu's or cable organiser 
    ## in a for loop one by one generate url for the object and genrate soup to pass to 
    ## the 'function get_shared_cpanel_server' 
    with open(html_file) as fp:
        soup = BeautifulSoup(fp, 'lxml')
   
    # give get_shared_cpanel_server function the soap to proceed  
    # Get dictionary for the object if is shared cpanel server
    #obj_dict = get_shared_cpanel_server(soup, "Shared cPanel") 
    #print_obj_dict(obj_dict)
    print_obj_dict(get_shared_cpanel_server(soup, "Shared cPanel"))

if __name__ == '__main__':
    main()
