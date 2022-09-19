file = open("demo2.txt", "a")
file.write("Hey there peeps")
file.close()

# Open and read the file after appending
file = open("demo2.txt", "r")
print(file.read())

# Overwrite the contents in a file
file = open("demo3.txt", "w")
file.write("Hey?? What's happening to me Arrrg!!")
file.close()

file = open("demo3.txt", "r")
print(file.read())

# Creating a new file
file = open("demo4.txt", "a")
file.write("What arggg!!!")
file.close()
