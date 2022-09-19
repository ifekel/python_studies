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



class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parents class"""
        super().__init__(make, model, year)
        self.battery = 85

    def batter_size(self):
        print(f"This car has a {self.battery}-kwh battery")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank")


my_tesla = ElectricCar("Mercedes Benz", "SUV", 2022)
print(my_tesla.get_descriptive_names())
my_tesla.batter_size()

myUsedCar = Car('Subaru', 2015, "outback")
print(myUsedCar.get_descriptive_names())

myUsedCar.update_odometer_reading(2500)
myUsedCar.get_odometer_reading()

myUsedCar.increment_odometer_reading(500)
myUsedCar.get_odometer_reading()