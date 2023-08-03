class GrandParent:
    def a1(self):
        print('2 Assets')

class Parent(GrandParent): # a1 & a2
    def a2(self):
        print('3 Assets')

class Son(Parent): # a1 , a2 & a3
    def a3(self):
        print('1 Asset')

obj1 = Son()
obj1.a1()
obj1.a2()
obj1.a3()