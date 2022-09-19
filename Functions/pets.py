# def pets(pet_type, pet_name):
#     print(f"My pet is a {pet_type}")
#     print(f"My {pet_type}'s name is {pet_name}! \n")
#     return
#
#
# pets("dog", "Dash")
# pets("cat", "Pills")

# Keyword Arguments

# def pets(pet_type, pet_name):
#     print(f"My pet is a {pet_type}")
#     print(f"My {pet_type}'s name is {pet_name}! \n")
#     return
#
#
# pets(pet_type="Dog", pet_name="Dash")
# pets(pet_type="Cat", pet_name="Milly")

# Using a default value parameter

def pets(pet_name, pet_type="dog"):
    print(f"My pet is a {pet_type}")
    print(f"My {pet_type}'s name is {pet_name}! \n")
    return


pets(pet_name="Dash")
pets(pet_name="Milly")
