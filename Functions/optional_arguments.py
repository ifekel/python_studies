def get_user_ID(first, last, middle=''):
    full_name = f"{first} {last} {middle}"
    return full_name.upper()

userID = get_user_ID("Onyekwelu", "Ifeanyi", "Anthony")
print(userID)