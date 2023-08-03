class Sample:
    a = 10
    b = 20
    def m1(self):
        print('Hi..Python')

obj1 = Sample() # Creating object for class
obj2 = Sample()

print(obj1.a)
print(obj1.a+obj2.b)
obj1.m1()
obj2.m1()

print(type(obj1))