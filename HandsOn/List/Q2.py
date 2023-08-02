n = int(input('Enter number of inputs: '))

index = []

for i in range(n):
    a = int(input('Enter # ' + str(i + 1) + ': '))
    index.append(a)

index2 = []
if n <= 6:
    print(index)
else:
    for i in range(3):
        index2.append(index[i])

    for i in range(n - 3, n):
        index2.append(index[i])

    print(index2)

