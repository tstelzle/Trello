import json
import csv
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

myLists = {}

for elem in data["lists"]:
    myLists[elem["id"]] = [elem["name"]]

for elem in data["cards"]:
    myLists[elem["idList"]].append(elem["name"])


myFile = open(sys.argv[2], 'w')

with myFile:
    writer = csv.writer(myFile)
    writer.writerows(myLists.values())

for (k,v) in myLists.items():
    print(v)
