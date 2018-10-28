uidset = set()
for user in pwd.get
import os, pwd

### This is equvalent to next peace of code  ###
### Creates a set of user id's in the system ###
# uidset = set()
# for line in open("/etc/passwd"):
#    split = line.split(":")
#    uidset.add(int(split[2]))

uidset = set()
for user in pwd.getpwall():
    uidset.add(user.pw_uid)

testdir= "/Users/akifyusein/paragon/paragon"

for folder, dirs, files in os.walk(testdir):
    for file in files:
        path = folder + "/" + file
        try:
            attributes = os.stat(path)
        except FileNotFoundError:
            print(path + " not found")
            continue
