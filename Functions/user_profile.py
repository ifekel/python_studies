def user_profile(first, last, **user):
    user['First name'] = first
    user['Last name'] = last
    return user


build_profile = user_profile("Onyekwelu", "Ifeanyi", age=17, gender="Male", heigth=178)
for item, items in build_profile.items():
    print(f"{item.upper()}: {items}")