import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from collections.abc import Iterable
from restaurant_management.dishes import Dish
from mixins.list_viewer import ListViewer

class Menu(ListViewer):
    def __init__(self, *dishes):
        self._dish_list = []
        if dishes:
            self.append_menu(dishes)

    def append_menu(self, dishes):
        if not isinstance(dishes ,Iterable):
            dishes = [dishes]
        for dish in dishes:
            if not isinstance(dish, Dish):
                raise ValueError('the input is invalid')
            if dish not in self._dish_list:
                self._dish_list.append(dish)

    def remove_from_menu(self, dish):
        if isinstance(dish, int):
            dish = self.get_dish_by_index(dish)
        elif not dish or dish not in self._dish_list:
            raise ValueError('dish is not in menu')
        self._dish_list.remove(dish)
     
    def get_dish_by_index(self, _index):
        if _index <= len(self._dish_list):
            return self._dish_list[_index-1]
        else:
            return False
    
    def _check_item(self, item):
        if isinstance(item, int):
            item = self.get_dish_by_index(item)
        elif not item or item not in self._dish_list:
            raise ValueError('dish is not in menu')
        return item
    
    def _get_dish_list(self, items):
        items = list(items)
        for i in range(len(items)):
            checked_item = self._check_item(items[i])
            items[i] = checked_item
        return items

    def view_menu(self):
        return self.view_list(self._dish_list, 'menu', enumerated=True)

    def creat_order(self, customer, *items):
        items = self._get_dish_list(items)
        customer.creat_order(*items)
    
    def add_to_order(self,order, *items):
        items = self._get_dish_list(items)
        order.add_to_order(*items)

    def remove_from_order(self, order, *items):
        items = self._get_dish_list(items)
        order.remove_from_order(*items)
        
