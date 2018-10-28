#!python

import sys

# if given arguments aaaa bbbb cccc
# create list starting from argument 1
# exclude argv[0] which is file_name
for arg in sys.argv[1:]:
    print(arg, end='\n')

