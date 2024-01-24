from abc import ABC, abstractmethod
import validations as valid
import sales_management.abs_purchase as purchase
import mixins.list_viewer as ls

class Purcheser(ABC,ls.ListViewer):
    '''represents a class of client'''
    _budget = valid.ValidNumber()
    _currency = valid.ValidCurrency()
    _currency = '$'
    def __init__(self) -> None:
        super().__init__()
        self._purchase_history = []
        self._budget = 0
    
    def set_curreccy(self, new_currency):
        self._currency = new_currency
    
    def increase_budget(self, amount):
        self._budget+=amount
        
    def request_fund(self, amount):
        return self._budget>=amount
    
    def view_purchase_history(self) -> None:
        '''displays purchase history'''
        return self.view_list(self._purchase_history, 'purchase history')
    
    def add_purchase(self, new_purchase):
        self._budget-=new_purchase.total_price
        self._purchase_history.append(new_purchase)
        return new_purchase

    def view_budget(self):
        return f'budget: {self._budget} {self._currency}'
    
    @abstractmethod
    def pay(self, item, salesperson = 'unknown'):
        ...
