class Father:
    def house(self):
        print('2 Flats and 2 Plots with house')

class Mother:
    def car(self):
        print('2 Cars')

    def cash(self):
        print('1 Billion cash')

class Son(Father,Mother):
    pass

obj1 = Son()

obj1.cash()
obj1.car()
obj1.house()