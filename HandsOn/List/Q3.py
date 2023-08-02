n = int(input('Enter number of inputs: '))

index = []
for i in range(n):
    a = int(input('Enter # ' + str(i + 1) + ': '))
    if a % 5 == 0:
        index.append(a)

print(index)