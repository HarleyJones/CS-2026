word = str(input('Enter a word to convert to pig latin:\n'))
for i, x in enumerate(word):
    lowercase_x = x.lower()
    if lowercase_x != 'a' or lowercase_x != 'e' or lowercase_x != 'i' or lowercase_x != 'o' or lowercase_x != 'u':
        print(f'{word[:i]}{word[i + 1:]}{x}ay'.lower())
        break