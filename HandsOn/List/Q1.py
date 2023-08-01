a = ['Python', 'Java', 'Ruby', 'Move', 'C++', 'Go', 'C', 'R', 'Swift', 'perl']

n = int(input('Enter the number of indexes: '))

indexes = []

for i in range(n):
     index =int(input('Enter index # ' + str(i+1) + ': '))
     indexes.append(index)


for i in indexes:
      print(a[i])

