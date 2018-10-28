
import collections

# constructor of defaultdict
hist = collections.defaultdict(int)

for line in opne("access.log"):
    url = line.split()[6].split('?')[0]
    hist[url] += 1

for url in sorted(hist, key=hist.get, reverse=True):
    if hist[url] < 50:
        break;
    print ("%-40s : %6d" %(url, hist[url]))