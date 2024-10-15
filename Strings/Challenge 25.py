firstname = input('Enter your first name:\n')
if len(firstname) < 5:
    surname = input('Enter your surname:\n')
    print(f'{firstname + } {surname}'.upper()}')
else:
    print(f'{firstname.lower()}')