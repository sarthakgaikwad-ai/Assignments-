import json

# Sample data (list of dictionaries)
data = [
    {"name": "Shreya", "age": 18, "city": "Pune"},
    {"name": "Amit", "age": 20, "city": "Mumbai"},
    {"name": "Riya", "age": 19, "city": "Delhi"}
]
# Create JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file created successfully !")

import json
import csv

# Read JSON file
with open("data.json", "r") as json_file:
    data = json.load(json_file)

# Write to CSV file
with open("data.csv", "w", newline="") as csv_file:
    headers = data[0].keys()  # Get column names
    
    writer = csv.DictWriter(csv_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data)

print("CSV file created successfully!")