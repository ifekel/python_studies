print("Welcome, To Who Wants to Be A Millionaire!")
print("Do you wish to play?")
print("You must be at least 10 - 60 years old to participate!")
print("If you met the age limit then go ahead and register")

playerName = input("Enter your name: ")
playerAge = int(input(f"Alright {playerName} enter your age: "))
balance = 30000

first_answer = "Mount Everest"
second_answer = "Rice"
third_answer = "Benjamin Franklin"

while True:
    if playerAge >= 10 or playerName == 60:
        print(f"Ok {playerName} you will be given N30,000 if you answer the first question correct")
        print("And your balance will increase as you answer each questions correctly")
        print("Are you ready?")
        play = input("> ").lower()

        if play == "yes":
            print("\tAlright, Here's your first question")
            print("What is the tallest mountain in the east")
            first_question = input("> ")

            if first_question == first_answer:
                print("is that your final answer: ")
                verified = input("> ").lower()
                if verified == "yes":
                    print("You are correct!")
                    print("You won N30,000")
                    balance = balance + 30000
                else:
                    print("Ok, which do you pick")
                    changed = input("> ")
                    if changed != first_answer:
                        print("You are wrong.")
                        print("But if you had gone for the first answer you would have been correct")
                        balance = balance - 30000
                        break
            else:
                print("is that your final answer: ")
                verified = input("> ").lower()
                if verified == "yes":
                    balance = balance - 30000
                    print("You are wrong!")
                    print("You go home with N0.00")
                    break

        print("\tAlright, Here's your second question")
        print("What is the most common food known to all Nigerians")
        second_question = input("> ")

        if second_question == second_answer:
            print("is that your final answer: ")
            verified = input("> ").lower()
            if verified == "yes":
                print("You are correct!")
                print("You won N100,000")
                balance = balance + 100000
                print(balance)
                break
            else:
                print("Ok, which do you pick")
                changed = input("> ")
                if changed != first_answer:
                    print("You are wrong.")
                    print("But if you had gone for the first answer you would have been correct")
                    balance = balance - 100000
                    break
        else:
            print("is that your final answer: ")
            verified = input("> ").lower()
            if verified == "yes":
                print("You are wrong!")
                print("You go home with N0.00")
                balance = balance - 100000
                break
