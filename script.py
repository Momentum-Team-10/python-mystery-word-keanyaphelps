import random
words = []
underscores = []
guesses = []
end_game = False


with open('words.txt') as file:
    strings = file.readlines()

    for string in strings:
        words.append(string)

    random_word = words[7].lower()
    random_word = random_word.replace("\n", "")
    print(random_word)

    word_length = range(len(random_word))
    for num in word_length:
        underscores.append('_')
    underscores = "".join(underscores)





