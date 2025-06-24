import csv
import json

rows = []
#reading from the csv file
try:
    with open("sample_names.csv","r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
except IOError as ex:
    print("Error performing I/O operations on the file: ",ex)

# writing to json file
try:
    with open("people.json", "w", encoding="utf-8") as f:
        # for row in rows:
        json.dump(rows, f, indent=4)
        rows.clear()
except IOError as ex:
    print("Error performing I/O operations on the file: ",ex)

#test

try:
    with open("people.json","r") as f:
        data = json.load(f)
except IOError as ex:
    print("Error performing I/O operations on the file: ",ex)
for i in data:
    print(i)



