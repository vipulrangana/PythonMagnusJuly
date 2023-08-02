n = int(input('Enter number of inputs: '))
rep = int(input('Enter number of repeating times: '))

index = []

for i in range(n):
    a = input('Enter # ' + str(i + 1) + ': ')
    for j in range(rep):
        index.append(a)

print(index)