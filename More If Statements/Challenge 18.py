num = int(input('Enter a number:\n'))

if num < 10:
    print(f'Too low')
elif 10 <= num <= 20:
    print(f'Correct')
else:
    print(f'Too high')