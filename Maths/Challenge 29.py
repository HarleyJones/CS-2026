import math

num = int(input('Enter a interger that is over 500\n'))
if num >= 500:
    print(str(round(float(math.sqrt(int(num*2))), 2)))
else:
    print('That number is less than 500')