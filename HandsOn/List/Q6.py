n = int(input('Enter number of inputs: '))

index = []

for i in range(n):
    a = input('Enter # ' + str(i + 1) + ': ')
    index.append(a)

tc = int(input('Enter number of test cases: '))

index2 = []
if tc > n:
    print('Invalid test case number')
else:
    for i in range(tc):
        index_no = int(input('Enter index number: '))
        if index_no > n - 1:
            index2.append('Invalid index no')
        else:
            index2.append(index[index_no])

for i in index2:
    print(i)
