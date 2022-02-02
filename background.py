import random
from PyQt5 import QtCore, QtGui, QtWidgets
class BadData(Exception):
    pass

class BadQuantity(Exception):
    pass

class Badformat(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'The {self.value} is in bad format or empty'

class Product:
    # ls = []

    def __init__(self, product, price, quantity):
        self.product = product
        self.price = float(price)
        self.quantity = int(quantity)
        self.__priority = self.calc_priority()



    def set_priority(self, n):
        self.__priority = n

    def get_priority(self):
        return self.__priority

    def __lt__(self, other):
        if isinstance(other, Product):
            if self.price == other.price:
                return self.__priority < other.__priority
            else:
                return self.price < other.price


    def calc_priority(self):
            return float(self.price) / (float(self.quantity) * 2)


    def __str__(self):
        return f'{self.product}, \t{self.price}, \t{self.quantity}'

    def __add__(self, other):
        if isinstance(other, Product):
            try:
                if float(self.price) + float(other.price) < 0:
                    raise BadData()
                else:
                    return Product(self.product, float(self.price) + float(other.price), self.quantity)
            except BadData:
                print('Bad Data')


def load():
    with open('warehouse_database.txt', 'r') as aru:
        l = []
        for line in aru:
            if line.count(' ') == 2:
                a,b,c = line.split(', ')
                l.append(Product(a, b, c))
    return l

#
if __name__ == '__main__':
    lista = load()
    lista.sort()
    for i in lista:
        print(i.__str__())
    # print(lista[0]+lista[2])
