import json

filename = "numbers.json"
with open(filename) as f:
    numbers = json.load(f)

print(numbers)

usernames = "usernames.json"
with open(usernames) as users:
    usernames = json.load(users)

for user in usernames:
    print(usernames)