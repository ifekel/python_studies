print("Give me two numbers, I'll add them together")
while True:
    try:
        first_number = int(input("Enter first number: "))
    except ValueError:
        print("Numbers only no alphabets")
    else:
        try:
            second_number = int(input("Enter second number: "))
        except ValueError:
            print("Numbers only no alphabets!")
        else:
            sum = first_number + second_number
            print(f"The sum of ({first_number}) and ({second_number}) is: {sum}")
    