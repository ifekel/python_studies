class Car:
    """A simple attempt to summarize a car"""

    def __init__(self, make, model, year):
        """Initialize attribute to describe a car"""
        self.year = year
        self.model = model
        self.make = make
        self.odometer = 0

    def get_descriptive_names(self):
        """return a neatly formatted description"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def get_odometer_reading(self):
        print(f"This car has a reading of {self.odometer} miles on it")

    def update_odometer_reading(self, mileage):
        """Set the odometer reading to the given value"""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer_reading(self, miles):
        self.odometer += miles


class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=87):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parents class"""
        super().__init__(make, model, year)
        self.battery = Battery()
