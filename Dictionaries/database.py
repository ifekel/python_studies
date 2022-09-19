print("Create a new account")
firstName = input("First name: ")
lastName = input("Last name: ")
new_password = input("password: ")
age = int(input("Age: "))
print("Account created successfully")

db_firstname = firstName
db_lastname = lastName
db_password = new_password
db_age = age

print("Now login")
username = input("Username: ")
password = input("Password: ")

if username == db_firstname and password == db_password:
    print("Welcome back", username)
else:
    print("No registered account with that username or password")






