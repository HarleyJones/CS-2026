word = str(input('Enter a word to convert to pig latin:\n'))
l1 = word[0]
if l1 == 'a' or l1 == 'e' or l1 == 'i' or l1 == 'o' or l1 == 'u':
    print(f'{word}way')
else:
    for i, x in enumerate(word):
        lowercase_x = x.lower()
        if lowercase_x != 'a' or lowercase_x != 'e' or lowercase_x != 'i' or lowercase_x != 'o' or lowercase_x != 'u':
            print(f'{word[:i]}{word[i + 1:]}{lowercase_x}ay'.lower())
            break