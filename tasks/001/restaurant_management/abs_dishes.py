import sys
import os
current_dir = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current_dir)
sys.path.append(parent)
import validations
from abc import ABC, abstractmethod

class Dish(ABC):
    currency = validations.ValidCurrency()
    currency = 'AMD'
    name = validations.ValidString()
    price = validations.ValidNumber()
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.dish_type = self.__class__.dish_type

    def __str__(self):
        return f"{self.name}: {self.price} {self.currency}"
    
    def view(self):
        return f'{self.dish_type}: {self.name}: {self.price} {self.currency}'
    @abstractmethod
    def serve(self):
        pass


class Hot:
    def heat(self):
        print('the dish is hot')

class Cold:
    def mix(self):
        print('mix and put together')

class Pourable:
    def pour(self):
        print('the dish is poured')

class Baked:
    def bake(self):
        print('the dish is baked')

class Cooked:
    def cook(self):
        print('the dish is cooked')


