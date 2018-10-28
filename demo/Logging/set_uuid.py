
# lsblk -n --output UUID /dev/sda1
# or
# blkid /dev/sda1

# Pseudo-Code
# for each line in fstab:
#   if the line contains a partition name
#       map the partititon name to a UUID using lsblk
#       write the modified line to the output file
#   else
#       copy the line to the output file unchanged

## regurla expresion for the line containig partition name
#  r"(/dev/sd[ab][0-9])(.*)"


# This is tested on centos7 and is working
# produce temp file and check if if fine then backup the fstab and copy new file to fstab
# Test if fstab is working with "mount -a", if no errors then everything is fine.
import re
from subprocess import Popen, PIPE

regex = re.compile(r"(/dev/sd[abcde][1-9])(.*)")

outfile = open ("fstab.out", mode="w")

for line in open("fstab.in"):
    match = re.search(regex, line)
    if match:
        print("Need to replace %s" % (match.group(1)))
        lsblk = Popen(["lsblk", "-n", "--output", "UUID",
                       match.group(1)], stdout=PIPE)
        #lsblk is in bynary format, that's why needs converting to string
        uuid = lsblk.stdout.readline().decode()
        # uuid[:-1] will remove new line "\n" from the line we read and concatinate with group 2 from regex
        replacement = "UUID=" + uuid[:-1] + re.sub(regex, r"\2", line)
        print("replacement line is %s" % replacement)
        print(replacement, end='', file=outfile)
    else:   #Copy line unchanged
        print(line, end='', file=outfile)
outfile.close()