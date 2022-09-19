class Restaurant:
    """Creating a model of a restaurant"""

    def __init__(self, name, cuisine):
        """Initialize the name and cuisine"""
        self.cuisine = cuisine
        self.name = name

    def describe_restaurant(self):
        print(f"{self.name} is a 5 star dinner")
        print(f"{self.name} is a cuisine of {self.cuisine} \n")

    def open_restaurant(self):
        print(f"{self.name} is OPEN!")

    def close_restaurant(self):
        print(f"{self.name} is CLOSED!")


dinner = Restaurant("Roots", "Chinese")
dinner1 = Restaurant("Crunches", "Brunch")
dinner2 = Restaurant("Ntachi-Osa", "Mama put")

dinner.describe_restaurant()
dinner1.describe_restaurant()
dinner2.describe_restaurant()

dinner.open_restaurant()
dinner.close_restaurant()
