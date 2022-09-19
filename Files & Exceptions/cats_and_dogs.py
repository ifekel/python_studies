def cats_and_dogs(cats_dogs):
    try:
        with open(cats_dogs, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        pass

    else:
        words = contents.strip()
        num_words = len(words)
        print(words)
        print(f"The file {cats_dogs} has {num_words} words")


filenames = ['cats.txt', 'dogs.txt', 'goats.txt']
for cats_dogs in filenames:
    cats_and_dogs(cats_dogs)