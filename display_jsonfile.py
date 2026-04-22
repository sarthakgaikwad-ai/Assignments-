import json

# Step 1: Create data
data = {
    "name": "Aman",
    "age": 20,
    "city": "Pune"
}

# Step 2: Create JSON file and write data
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file created.\n")

# Step 3: Read and display content
with open("data.json", "r") as file:
    content = json.load(file)

print("Content of JSON file:")
print(content)