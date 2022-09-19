from car import Car

myNewCar = Car("audi", "a4", 2019)
print(myNewCar.get_descriptive_names())

myNewCar.odometer = 30
myNewCar.get_odometer_reading()