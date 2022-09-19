def album(artiste, album):
    data = f"Artiste: {artiste}, Album: {album}"
    return data


while True:
    print("\n Enter your  name!")

    print("Enter 'q' to quit")
    artiste = input("Musician: ")
    if artiste.lower() == "q":
        break

    print("Enter 'q' to quit")
    album_name = input("Album title: ")
    if album_name.lower() == "q":
        break

    music = album(artiste, album_name)
    print(music)
