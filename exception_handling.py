filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:\n")
        print(content)

except FileNotFoundError:
    print(" Error: The file does not exist. Please check the filename.")

except PermissionError:
    print("Error: You do not have permission to read this file.")