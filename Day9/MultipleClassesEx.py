class Sample:
    def m1(self):
        print('Welcome m1 function')

class Demo(Sample):
    def m2(self):
        print('Welcome m2 function')

obj1 = Demo()

obj1.m1()
obj1.m2()
