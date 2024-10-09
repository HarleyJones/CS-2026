firstname = str(input('Enter your first name in lowercase:\n'))
surname = str(input('Enter your surname in lowercase:\n'))
full_name = str(f'{firstname.title()} {surname.title()}')
print(f'{full_name}')