import os
import json

clist = r'C:\xampp\htdocs\data\countries_list.txt'
cvisited = r'C:\xampp\htdocs\data\countries_visited.json'

## Read list into dictionary
data = []
lastcountry = "ES"
with open(clist) as fp:  
	for cnt, line in enumerate(fp):	
		country = line.rstrip()
		print cnt, country	
		if country:
			data.append({"e": lastcountry, "i": country, "v": 1000000})
			data.append({"e": country, "i": lastcountry, "v": 1000000})			

## Dump json
with open(cvisited, 'w') as outf:
	json.dump(data, outf)
