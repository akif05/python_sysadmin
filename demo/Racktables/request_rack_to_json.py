import requests
import sys
import json

username='aaaaa'
password='bbbbb'

r = requests.get('https://racktables-001.sl5.misp.co.uk/racktables/index.php?page=depot', auth=('parayusein', 'Fik@r15082'))


## Thise are working examples!!!
# with open('new_whit_whit.html', 'w') as f:
#    print(r.text, file=f)


# r = requests.get('https://racktables-001.sl5.misp.co.uk/racktables/index.php?page=depot', auth=('parayusein', 'Fik@r15082'))
# sys.stdout=open('new_wiht_open.html', 'w')
# print(r.text)
# sys.stdout.close()


