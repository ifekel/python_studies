# def pizzaToppings(*toppings):
#     print("The pizza toppings you requested for:")
#     for topping in toppings:
#         print(f"-{topping}")
#
#
# pizzaToppings("beef")
# pizzaToppings("Chicken", "Pepperoni", "Beef")

# EDITED

def pizzaToppings(size, *toppings):
    print(f"You ordered a {size} inch pizza with the following toppings")
    for topping in toppings:
        print(f"-{topping}")

