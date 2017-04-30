import json
import sys
from glob import glob


S = '{{"index":{{"_id":"{0}"}}}}\n{1}\n\n'

outlist = []

for infile in glob('json_bank/*'):
    with open(infile, 'r') as of:
        f = json.loads(of.read())
        outlist += f['certificates']

with open('outfile.txt', 'w') as of:
    for _id, obj in enumerate(outlist):
        of.write(S.format(_id, obj))

print ":)"
