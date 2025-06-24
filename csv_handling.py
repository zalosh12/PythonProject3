import csv
from dataclasses import field

#question 7

try:
    with open("sample_names.csv","r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"my name is: {row['GivenName']}, " +
                f"I live in {row['City']} " +
                f"and I work at {row['Occupation']}, "+
                f"My gender is {row['Gender']}")
except IOError as ex:
    print("Error performing I/O operations on the file: ",ex)

#question 8

def add_record():

    name = ""
    while not name.isalpha() or len(name) < 2:
        name = input("Enter your name: ").strip().title()

    gender = ""
    while gender not in ["Male","Female"]:
        gender = input("enter you gender(Male/female): ").strip().capitalize()

    title = ""
    while title not in ["Mr.","Ms.","Mrs."]:
        title = input("Enter your title(Mr.,Ms,Mrs.: ").title()

    occupation = ""
    while not occupation.isalpha() or len(occupation) < 2:
        occupation = input("Enter your occupation: ").strip().title()

    city = ""
    while not city.isalpha() or len(city) < 2:
        city = input("Enter your city: ").strip().title()

    record = {
        "GivenName": name,
        "Gender": gender,
        "Title": title,
        "Occupation": occupation,
        "City": city
    }

    return record

def add_to_file(file_name,record):
    try:
        with open(file_name,"a",newline="") as file:
            field_names = ["GivenName","Gender","Title","Occupation","City"]
            writer = csv.DictWriter(file,fieldnames=field_names)

            writer.writerow(record)
            print("the record added successfully")
    except IOError as ex:
        print("Error performing I/O operations on the file: ", ex)


if __name__ == "__main__":
    new_record = add_record()
    add_to_file("sample_names.csv",new_record)








