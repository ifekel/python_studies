# def buildID(first, last):
#     person = {"first name": first, "last name": last}
#     return person
#
# musicain = buildID("Onyekwelu", "Ifeanyi")
# print(musicain)


def buildID(first, last, age=None):
    person = {"first name": first, "last name": last}
    if age:
        person['age'] = age
    return person

musicain = buildID("Onyekwelu", "Ifeanyi", 17)
print(musicain)