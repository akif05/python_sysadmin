import requests
import sys
import json
import configparser

# https://stackoverflow.com/questions/924700/best-way-to-retrieve-variable-values-from-a-text-file-python-json
# read configuration from file
# file format

#$ cat ~/.my_a_pass
# [myvars]
# username: my_username
# passwd: my_password

config = configparser.ConfigParser()
config.read("/Users/akifyusein/.my_a_pass")

password = config.get("myvars", "passwd")
username = config.get("myvars", "username")

<<<<<<< HEAD
r = requests.get('https://racktables-mysite.co..uk/racktables/index.php?page=depot', auth=(username, password))



#r = requests.get('https://racktables-001.sl5.misp.co.uk/racktables/index.php?page=depot', auth=(''))
=======
r = requests.get('https://racktables-mysite.co.uk/racktables/index.php?page=depot', auth=(username, password))




>>>>>>> 7f151a5cc833a40a859d1aa49399a6918b775f4d

## F string examples
# print(f'Username: {username}')
# print(f'passwd: {password}')

## Thise are working examples!!!
# with open('new_whit_whit.html', 'w') as f:
#    print(r.text, file=f)



# sys.stdout=open('new_wiht_open.html', 'w')
# print(r.text)
# sys.stdout.close()
