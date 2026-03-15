import os

if os.path.exists("data.txt"):
    print("File exists")
    # File Read
    file = open("data.txt", "r")
    print(file.read())
    file.close()
else:
    print("File not found")
    # File Write Write (overwrite)
    file = open("data.txt", "w")
    file.write("Hello Python")
    file.close()
    

# File Append
file = open("data.txt", "a")
file.write("\nNew Line Added")
file.close()


with open("data.txt", "r") as file:
    data = file.read()
    print(data)
    

# Read first 10 characters
file = open("data.txt", "r")
print(file.read(10))
file.close()


# Read line by line
file = open("data.txt", "r")
for line in file:
    print(line)
file.close()


# File Delete
# import os
# os.remove("data.txt")