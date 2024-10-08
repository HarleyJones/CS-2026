raining = str(input('Is it raining?:\n'))

if raining.lower() == 'yes':
   windy = str(input('Is it windy?:\n'))
   if windy.lower() == 'yes':
       print(f'It is too windy for an umbrella')
   else:
       print(f'Take an umbrella')
else:
    print(f'Enjoy your day')