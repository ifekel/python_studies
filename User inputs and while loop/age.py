age = int(input("What is your age? "))
print(f"Your age is {age}")

if age < 18:
    print("You are too young to sign up")
elif age > 50:
    print("You are too old to sign up")
else:
    print("Registration successful")
