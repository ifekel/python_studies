# file = open("demo.txt", "r")
# print(file.read())

# Specify how many character to read from the file
file = open("demo.txt", "r")
# print(file.read(10))

# Return the first line of the file
# file = open("demo.txt", "r")
# print(file.readline())

# Return the first two lines of the file
# file = open("demo.txt", "r")
# print(file.readline())
# print(file.readline())

# Looping through the file
for x in file:
    print(x)

# Closing the file
file.close()
