firstname = str(input('Enter your first name:\n'))
if len(firstname) < 5:
    surname = str(input('Enter your surname:\n'))
    print(f'{f'{firstname} {surname}'.upper()}')
else:
    print(f'{firstname.lower()}')