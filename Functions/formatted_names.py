def get_formatted_names(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.upper()

musicians = get_formatted_names("Onyekwelu", "Ifeanyi")
print(musicians)