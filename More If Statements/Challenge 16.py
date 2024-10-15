raining = str(input('Is it raining?:\n')).lower() 

if raining == 'yes':
   windy = str(input('Is it windy?:\n')).lower()
   if windy == 'yes':
       print('It is too windy for an umbrella')
   else:
       print('Take an umbrella')
else:
    print('Enjoy your day')