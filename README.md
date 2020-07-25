# Trello

A simple script to extract the data from a trello board. The data from trello has to be in a json format and will be outputted as a csv.

## Instructions
There are to different scripts available ('trello_1.py' and 'trello_2.py'). 
The scripts have the same functionality, but work with different logic. 
It is recommended to use 'trello_1.py'.

### Usage
The script will be started with two arguments. 
The first is the json file, in which the trello data is written. 
The second is the file to the csv file.

### Running
For the script to work you will need to install python on your machine.
No extra dependencies are needed.
To run the script use the following command. 

```Shellscript
python trello_1.py <input.json> <output.csv>
```

or 

```Shellscript
python trello_2.py <input.json> <output.json>
```

Where <input.json> and <output.json> correspond to the arguments mentioned above.

