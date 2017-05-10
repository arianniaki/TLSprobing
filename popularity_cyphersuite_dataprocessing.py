from glob import glob
import re
from csv import DictReader
from collections import defaultdict

def inner_dict_init():return defaultdict(float)
protocols = defaultdict(inner_dict_init)


for infile in  glob('TLS1_bank/*'):
    with open(infile, 'r') as of:
        reader = DictReader(of)
        for row in reader:
            for p in row:
                if not p:continue
                item = row[p]
                cipher, value = item.split()
                cipher = cipher.translate(None, "{'}:")
                value = value.translate(None, "{}, ''")
                protocols[p][cipher]+=float(value)

# print protocols
res = {}
for p in protocols:
    a = sorted(protocols[p], key = lambda x: protocols[p][x], reverse=True)
    res[p] = [(i, protocols[p][i]) for i in a][:5]
    res[p].append(('other', sum([protocols[p][i] for i in a][5:])))

for p in res:
    print p
    for i, j in res[p]:
        print '{0},{1}'.format(i,j)
