magicians = ['Alice', 'David', 'Caroline']
for magician in magicians:
    print(magician)
print("\n")
# Doing more withing a for loop
for magician in magicians:
    print(f"{magician.title()}, that was great trick")
    print(f"i can't wait to see your next trick, {magician.title()}\n")
print(f"Thank you, everyone. That was a great magic show!")
