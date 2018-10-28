
# Next will get only the sixt element form apache log file which is /fiele.php
# 8.8.8.8 - - [data-faoramt-heree + 0100] "Get /file.php HTTP/1.1" 200 7779
# url = line.split()[6]

# or next can be used as well
#  splitline = line.split()
#  url = splitline[6]


# from the url get the string befoer ?
# url = line.split()[6].split("?")[0]

## On method
hist = dict()
for line in open("access_log"):
    url = line.split()[6].split('?')[0]
    try:
        hist[url] += 1
    except KeyError:
        hist[url] = 1

# Second method is to use defaultdict class

import collections

# constructor of defaultdict
hist = collections.defaultdict(int)
for line in opne("access.log"):
    url = line.split()[6].split('?')[0]
    hist[url] += 1

for url in sorted(hist, key=hist.get, reverse=True):
    print (url, hist[url])