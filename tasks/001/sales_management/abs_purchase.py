import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import validations as valid
from mixins.object_with_id import ObjectWithID


class Purchase(ObjectWithID):
    '''represents a class of purchases'''
    total_price = valid.ValidNumber()
    currency = valid.ValidCurrency()
    def __init__(self, customer, salesperson, item, total_price, currency = '$') -> None:
        self._id = self._count_id()
        self.customer = customer
        self.salesperson = salesperson
        self.item = item
        self.total_price = total_price
        self.currency = currency

    def view(self):
        '''returns a long description of an item'''
        return f'purchase {self._id}\n{self.customer}\nsalesperson: {self.salesperson}\nitem: {self.item}\ntotal: {self.total_price:.2f} {self.currency}'
    
    def __str__(self):
        return f'id {self._id}: {self.total_price}'