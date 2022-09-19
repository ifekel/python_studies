class User:
    def __init__(self, username, age, password):
        self.password = password
        self.username = username
        self.age = age

    def userID(self):
        print("\tFill the registration form\n")
        db = {}
        while True:
            self.username = input("Enter a username: ")

            if len(self.username) < 3:
                print("Username is too short!")
            elif len(self.username) > 20:
                print("Username is too long!")
            else:
                db["Username"] = self.username
                self.age = int(input("Enter your age: "))
                if self.age < 18:
                    print("You must be at least 18 years or older to register")
                else:
                    db["Age"] = self.age
                    self.password = input("Enter a password: ")
                    if len(self.password) < 8:
                        print("Password is too short!")
                    elif len(self.password) > 20:
                        print("Password is too long!")
                    else:
                        db["Password"] = self.password
                        print("Registration successful")
                        break


userCreation = User("Ifeanyi", 17, "Ifyonyekeshy7")
print(userCreation.userID())
