a1 = [10,30,23,'abc',10.2,'hello']
print(a1)
print(a1[1])
print(a1[0:4])
print(a1[3:6])
print(a1[2:])
print(a1[:5])

a1.append(120)
print(a1)
a1.remove(30) #remove a record by value
print(a1)
a1.insert(1,30) #Insert new value
print(a1)
a1[3]= 50 #Replacing
print(a1)
a1.pop() #Delete the last record of the index
print(a1)
a1.pop(1) #Delete the record from index number
print(a1)

