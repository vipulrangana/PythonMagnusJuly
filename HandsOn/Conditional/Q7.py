n1 = str(input('Enter a 2 digit number: '))
n3 = int(n1)

n2 = []
for i in n1:
    digit = int(i)
    n2.append(digit)

a = n2[0]
b = n2[1]

if (a+b) == 7:
    print('Special Number')
elif a == 7 or b == 7:
    print('Special Number')
elif n3%7 == 0:
    print('Special Number')
else:
    print('Normal Number')


