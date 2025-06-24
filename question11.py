import json

try:
    with open("people.json","r") as f:
        data = json.load(f)
except IOError as ex:
    print("Error performing I/O operations on the file: ",ex)

count_people_by_city = {}
for person in data:
    city = person["City"]
    count_people_by_city[city] = count_people_by_city.get(city,0) + 1

for city,count in count_people_by_city.items():
    print(f"The number of people in {city}: {count}")
