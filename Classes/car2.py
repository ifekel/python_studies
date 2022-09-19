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


myNewCar = Car("Mercedes Benz", 2022, "GLX 360")
print(myNewCar.get_descriptive_names())
myNewCar.odometer = 20
myNewCar.get_odometer_reading()