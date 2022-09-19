def get_formatted_names(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.upper()


while True:
    print("\n Enter your name!")
    f_name = input("First name: ")
    if f_name.lower() == "q":
        break
    l_name = input("Last name: ")
    if l_name.lower() == "q":
        break

    formattedNames = get_formatted_names(f_name, l_name)
    print(f"\nHello {formattedNames}")
