import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import order_management.general_clients as client
from product_management.rates import Rater
from product_management.reviews import Reveiwer
from mixins.item_searcher import ItemSearcher

class Customer0(client.Client, Reveiwer, Rater, ItemSearcher):
    currency = '$'
    def search(self, search_list, *, description = None, name = None, product_type = None, min_price = 0, max_price = None, display = False, **kwargs) -> None:
        '''seraches an item by given charecteristics in a given list and displays search result'''
        properties_by_value = {'product_type': product_type}
        producties_by_text = {"name": name, 'description': description}
        res = self._search(search_list, value_property_list=properties_by_value,text_property_list=producties_by_text, min_salary=min_price, max_salary=max_price)
        
        if display:
            print(self.view_list(res, 'search resuls'))
        return res
    

class Customer(client.Client, Reveiwer, Rater, ItemSearcher):
    currency = '$'
    def search(self, search_list, *, min_price = 0, max_price = None, display = False, **kwargs) -> None:
        '''seraches an item by given charecteristics in a given list and displays search result'''
        producties_by_text = kwargs
        res = self._search(search_list, value_property_list={},text_property_list=producties_by_text, min_salary=min_price, max_salary=max_price)
        
        if display:
            print('result of search:')
            print(self.view_list(res, 'search resuls'))
        return res