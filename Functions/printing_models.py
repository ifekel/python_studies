# unprinted_designs = ["Phone case", "Robot pendant", "dodecahedron"]
# completed_designs = []
#
# while unprinted_designs:
#     current_models = unprinted_designs.pop()
#     print(f"Printing model: {current_models}")
#     completed_designs.append(current_models)
#
# print("\nThe following models have been printed:")
# for completed_design in completed_designs:
#     print(completed_design)

# Reorganizing the program with two functions

def print_models(unprinted_designs, completed_designs):
    """
    Simulate printing each design. until none are left
    Move each design to completed_design after printing
    """

    while unprinted_designs:
        current_models = unprinted_designs.pop()
        print(f"Printing model: {current_models}")
        completed_designs.append(current_models)

def show_completed_designs(completed_designs):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_design in completed_designs:
        print(completed_design)


unprinted_designs = ["Phone case", "Robot Pendant", "Dodecahedron"]
completed_designs = []

print_models(unprinted_designs[:], completed_designs)
show_completed_designs(completed_designs)

# print(unprinted_designs)