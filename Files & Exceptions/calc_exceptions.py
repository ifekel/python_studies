print("Give me two numbers, I'll divide them.")
print("Enter 'q' to quit.")

# while True:
#     first_number = input("Enter first number: ")
#     if first_number == "q":
#         break
#
#     second_number = input("Enter second number: ")
#     if second_number == "q":
#         break
#
#     answer = int(first_number) / int(second_number)
#     print(f"Answer in decimal: {answer}")
#     print(f"Answer rounded up: {int(answer)}")
#
#
# Format the code with try except
while True:
    first_number = input("Enter first number: ")
    if first_number == "q":
        print("Quitted!")
        break


    second_number = input("Enter second number: ")
    if second_number == "q":
        print("Quitted!")
        break

    try:
        answer = int(first_number) / int(second_number)

    except ZeroDivisionError:
        print("You cannot divide a number with 0")

    else:
        print(f"Answer in decimal: {answer}")
        print(f"Answer rounded up: {int(answer)}")



