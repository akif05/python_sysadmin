Akifs-Mac:Racktables akifyusein$ for i in ./*.py; do echo "$i"; cat $i; echo; done
./func.py
import requests
from bs4 import BeautifulSoup
import lxml.html as lh
import pandas as pd
import re
import sys
import configparser
import os.path

def get_request_url_data(auth_file, url):
    
    config_file = auth_file
    url_loc = url

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
    
    ## Return r which is obtained from requests.
    return r
### end ########################################

def get_all_object_by_id(soup):

    urls = []
    exlude_list = ["CableOrganizer", "Organizer", "spacer", "PDU", "Shelf", "PatchPanel"]

    obj_base_url = "https://racktables-001.sl5.misp.co.uk/racktables/index.php?page=object&tab=default&object_id="
    div = soup.find("div", {"class":"portlet"})
    table = div.find("table")
    rows = table.find_all("tr", {"class": ["row_odd", "row_even"]})
    for row in rows:
        tmp = str(re.findall(r'<strong>(.*?)</strong>', str(row.find_all('strong'))))
        if any (x in tmp for x in exlude_list): 
            continue
        # Sometime returns two list of two value, extract the first one
        obj_id = re.findall(r'object_id=([0-9]*)">', str(row))
        obj_id = str(obj_id[0].strip("[]'"))
        # obj_id = str(re.findall(r'object_id=([0-9]*)">', str(row))).strip("[]'")
        url = """%s%s""" % (obj_base_url, obj_id)
        urls.append(url)

    # Return list of objects url with object id to retrive information for each object 
    return urls

### end ########################################
def print_obj_dict(object_dict, obj_num):
    line = "=" * 50
    explisit_tags=object_dict.get('Explicit_tags')
    common_name = object_dict.get('Common_name')
    asset_tag = object_dict.get('Asset_tag')
    fqdn = object_dict.get('FQDN')

    s = """Object Num: %s\nFQDN: %s\nCommon name: %s\nExplisit tags: %s\nTag: %s """ \
     % ( obj_num, fqdn, common_name, explisit_tags, asset_tag)

    print(line)
    print(s)
    print(line)
### end ########################################

./get_objects_info.py
def get_objects_info(beauty_soap):

    key_list = []
    value_list = []
    object_dict = {}
    line = "=" * 50

    div = beauty_soap.find("div", {"class":"portlet"})
    table = div.find("table")
    rows = table.find_all("tr")

    for row in rows:
        if hasattr(row.th, 'text'):
            key_list.append(str(row.th.text.strip().strip(":").replace(" ", "_")))
        else:
            key_list.append("No_key")

        if hasattr(row.td, 'text'):
            value_list.append(str(row.td.text.strip()))
        else:
            value_list.append("No_value")

    # object_dict = dict(zip(key_list, value_list))
    return dict(zip(key_list, value_list))



./is_object_in.py
def is_object_in(dict_obj, key, val):

    ## If is dictionary get the values for the key
    ## if the valie is not string return false
    if hasattr(dict_obj, 'get'):
        value = dict_obj.get(key)
        if isinstance(value, str) == False:
            return False
    else:
        return False
    
    ## Check if the value is list or string and is lookup string we
    ## Are looking for. If yes return True if not retrun False
    if val in value:
        return True
    else:
        return False

./main.py
import requests
from bs4 import BeautifulSoup
import lxml.html as lh
import pandas as pd
import re
import sys
import configparser
import os.path
from func import *
from get_objects_info import *
from is_object_in import *

def main():

    line = "=" * 50
    # explisit_tag = "Shared cPanel"
    explisit_tag = "available stock"
    url_gl = "https://racktables-001.sl5.misp.co.uk/racktables/index.php?page=depot"
    config_file = "/Users/akifyusein/.my_a_pass"
    req = get_request_url_data(config_file, url_gl)
    soup = BeautifulSoup(req.text, 'lxml')

    # Create urls for all objects except PDU and cable organizer
    urls = get_all_object_by_id(soup)
    soup = ""
    # From each url in list get data and find objects with explisit tag Shared cPanel
    i = 0
    for url in urls:
        i += 1
        if i > 3:
            sys.exit(1)
        try:
            req = get_request_url_data(config_file, url)
        except:
            print(f'Can not retrive: {url}')
            continue
        soup = BeautifulSoup(req.text, 'lxml')
        obj_dict = get_objects_info(soup)

        ## Get the key and lookup from command line!
        key = 'Explicit_tags'
        lookup = 'managed'
        # lookup = 'available stock'
        flag = is_object_in(obj_dict, key, lookup)

        if flag == True:
            # Get the object num form url and print out for user info.
            object_number = str(re.findall(r'object_id=([0-9]*)', url)).strip("[]'") 
            print_obj_dict(obj_dict, object_number)
        else:
            continue
 
if __name__ == '__main__':
    main()



## Hypervisor: Yes
## Common name: hvhost-008
## Contains: [ list of vms.......]
## Object type: Server
## Explicit tags: Tanium
## Asset tag:

