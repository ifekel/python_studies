def album(artiste, album, songs=None):
    data = {"Artiste": artiste, "Album": album}

    if songs:
        data["songs"] = songs

    return data

music = album("Burna Boy", "Love Damini", 20)
print(music)

