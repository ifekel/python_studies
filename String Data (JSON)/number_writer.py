import json

numbers = [2, 3, 5, 7, 11, 13, 17, 19, 21, 23]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
