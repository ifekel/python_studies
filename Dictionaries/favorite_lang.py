person = {
    'amanda': 'C++',
    'Joseph': 'C',
    'Kelvin': 'Kotlin',
    'Ifeanyi': 'Python',
    'Mathew': 'Swift'
}
print(f"Mathew's favorite language is {person['Mathew']}")

#  using get()

another_person = person.get('Jack', 'PHP')
print(person)
print(another_person)
