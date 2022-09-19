def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()

    except FileNotFoundError:
        print(f"The file {filename} could not nbe found")

    else:
        # Count the number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has a total of {num_words} words")


filenames = ['demo2.txt', 'demo3.txt', 'demo4.txt']
for filename in filenames:
    count_words(filename)