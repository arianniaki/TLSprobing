import sys
import json

subnet_file_name = sys.argv[1]
outlist = []
with open(subnet_file_name, 'r') as of:
	line = of.read()
	filedata = line.replace('\"}"', '\",\\"university\\": \\"Yale University\\"}\"')

# Write the file out again
with open('final_Yale University_servers.txt_curl.json', 'w') as file:
  file.write(filedata)

