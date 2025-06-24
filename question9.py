import csv
from dataclasses import field

#creating a dictionary from the original file
try:
    with open("sample_names.csv","r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        result_dict = {}
        for row in reader:
            city = row["City"]
            title = row["Title"]
            if city not in result_dict:
                result_dict[city] = {title: 1}
            else:
                if title in result_dict[city]:
                    result_dict[city][title]+= 1
                else:
                    result_dict[city][title] = 1
except IOError as ex:
    print("Error performing I/O operations on the file: ",ex)

#writing the dictionary to a new file
try:
    with open("city_summary.csv", "w", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["City","Subject","Count"])
        for city,subjects in result_dict.items():
            for subject in subjects:
                writer.writerow([city,subject,subjects[subject]])
except IOError as ex:
    print("Error performing I/O operations on the file: ",ex)

#test the result
with open("city_summary.csv","r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)