age = int(input('How old are you?:\n'))

if age >= 18:
    print(f'You can vote')
elif age == 17:
    print(f'You can learn to drive')
elif age == 16:
    print(f'You can buy a lottery ticket')
else:
    print(f'You can go Trick-or-Treating')