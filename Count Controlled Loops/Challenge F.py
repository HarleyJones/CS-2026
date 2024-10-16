num = int(input("Enter a number between 1 and 12: "))

if 1 < num <= 12:
    for i in range(12):
        print((i + 1) * num)
else:
    print("Not between 1 and 12")