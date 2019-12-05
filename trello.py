import json
import sys
import csv

# open json file
with open(str(sys.argv[1]), 'r') as myfile:
    data=myfile.read()
obj = json.loads(data)

#get all cards in the board session
karten = []
for card in obj['cards']:
    karten.append((card['name'], card['idList']))

#get all lists in the board session
listen = []
for list in obj['lists']:
    listen.append((list['name'], list['id']))

all_events = []

for list in listen:
    event = [list[0]]
    for card in karten:
        if list[1] == card[1]:
            event.append(card[0])
    all_events.append(event)

#get all cards with some kinde of label, in the current session only the places are labeled
#orte = []
#orte_2 = []
#string = "5d80cba6af988c41f2a84190"
#for karte in obj['cards']:
    #if string in karte['idLabels']:
    #   orte.append((karte['name'], karte['idList']))
#    if karte['idLabels']:
#       orte_2.append((karte['name'], karte['idList']))

#new_list = []
#for ort in orte_2:
#    for list in listen:
#        if ort[1] == list[1]:
#            new_list.append([list[0], ort[0]])

print(all_events)

csvfile =  open(str(sys.argv[2]), 'w', newline="")
with csvfile:
    writer = csv.writer(csvfile)
    #for elem in all_events:
    writer.writerows(all_events)
