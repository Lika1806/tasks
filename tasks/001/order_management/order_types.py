from collections import defaultdict
import validations as valid
from mixins.object_with_id import ObjectWithID
from order_management.order_exceptions import ClosedOrderError
from abc import ABC, abstractmethod

class AbstractOrder(ABC,ObjectWithID):
    '''represents a class of purchases'''
    _total_price = valid.ValidNumber()
    def __init__(self, customer, item_list = None) -> None:
        super().__init__()
        self._total_price = 0
        self.customer = customer
        if item_list:
            self.add_to_order(*item_list)

    def add_to_order(self, *items):
        if not self._check_access():
            raise ClosedOrderError
        for item in items:
                self._add_item(item)

    def remove_from_order(self, *items):
        if not self._check_access():
            raise ClosedOrderError
        for item in items:
            if item in self.item_list:
                self._remove_item(item)
            else:
                raise ValueError('Item is not in the list')
    
    def get_order(self, order, order_list):
        if isinstance(order, int):
            return self._get_item_by_id(order, order_list)
        if order in order_list:
            return order
        raise None

    def _check_access(self):
        return True
        
    @property
    def total_price(self):
        return self._total_price

    @property
    def currency(self):
        return '$'
    
    @abstractmethod
    def _add_item(self, *items):
        ...
    @abstractmethod
    def _remove_item(self, *items):
        ...    

    

class OrderWithRepeatedItems(AbstractOrder):
    def __init__(self, customer, item_list=None) -> None:
        self._item_list = defaultdict(int)
        super().__init__(customer, item_list)
    
    def _add_item(self, item):
        self._item_list[item]+=1
        self._total_price+=item.price

    
    def _remove_item(self, item):
        self._item_list[item]-=1
        if self._item_list[item]==0:
            self._item_list.pop(item)
        self._total_price-=item.price
    
    @property
    def item_list(self):
        return self._item_list.keys()
    
class OrderWithUniqueItems(AbstractOrder):
    def __init__(self, customer, item_list=None) -> None:
        self._item_list = []
        super().__init__(customer, item_list)
    
    def _add_item(self, item):
        self._item_list.append(item)
        self._total_price+=item.price
    
    def _remove_item(self, item):
        self._item_list.remove(item)
        self._total_price-=item.price

    @property
    def item_list(self):
        return self._item_list[:]
    