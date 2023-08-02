a = int(input('Enter the score A: '))
b = int(input('Enter the score B: '))

if a > 300 or b > 300:
    if (a+b) < 500:
        print('Can Team Up')
    else:
        print('Cannot Team Up')
else:
    print('Cannot Team Up')
