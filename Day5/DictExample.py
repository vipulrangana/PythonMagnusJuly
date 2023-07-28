d1 = {101:'abc',102:'bcd',103:'cde'}
print(type(d1))
print(d1[101])
print(d1)
d1[104]= 'efg' #add a new record
d1[102]= 'xyz' #replace the existing vale of the key
print(d1)
d1.pop(103) #remove a record
print(d1)