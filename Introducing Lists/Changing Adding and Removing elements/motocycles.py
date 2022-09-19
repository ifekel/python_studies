motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Changing elements in the list
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)

# Adding items to an empty list
sportCars = []  # An empty list
print(sportCars)

sportCars.append("Lamborghini")
print(sportCars)
sportCars.append('Ferrari')
print(sportCars)
sportCars.append('Bugatti')
print(sportCars)

# Inserting new elements into a list
print(sportCars)
sportCars.insert(3, 'Bentley')
print(sportCars)
sportCars.insert(4, 'Suburban')
print(sportCars)

# Removing elements from a list
print(sportCars)
del sportCars[4]
# sportCars.remove('Bentley')
print(sportCars)

print(sportCars)
too_expensive = 'Lamborghini'
sportCars.remove(too_expensive)
print(sportCars)
print(f"\nA {too_expensive.title()} is too expensive for me.")
