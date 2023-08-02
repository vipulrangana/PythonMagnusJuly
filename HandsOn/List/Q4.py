L = ["apple", "78", "970.03"]

n = int(input('Enter number of inputs: '))

for i in range(n):
    a = input('Enter # ' + str(i + 1) + ': ')
    L.append(a)

print(L)