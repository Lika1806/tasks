import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import validations as valid
from abc import ABC, abstractmethod
import mixins.list_viewer as ls

class AbstractSalesperson(ABC,ls.ListViewer):
    '''represents a class of salespeople'''
    commision = valid.ValidNumber()
    def __init__(self, commision = 0) -> None:
        super().__init__()
        self._sales_history = []
        self.commision = commision

    def set_commision(self, value):
        self.commision = value

    @abstractmethod
    def add_sale(self, purchase) -> None:
        '''adds sale to sales history'''
        self._sales_history.append(purchase)

    @abstractmethod
    def view_sales_history(self) -> None:
        '''displays purchase history'''
        return self.view_list(self._sales_history, 'sales history')