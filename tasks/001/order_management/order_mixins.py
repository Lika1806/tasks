import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from mixins.list_viewer import ListViewer
import validations as valid
import sales_management.abs_purchase as sm
from order_management.order_exceptions import ClosedOrderError
from abc import ABC,abstractmethod

class ViewableOrder(ListViewer):
    '''Represents a class of viewable orders'''
    def __str__(self):
        return f'order {self.item_id}: {self.total_price} {self.currency}'
    
    def view(self):
        '''Returns a detailed description of an item.'''
        return f'order {self.item_id} status: {self._status}\ncustomer: {self.customer}\ntotal: {self.total_price:.2f} {self.currency}'
    
    def view_order_list(self):
        '''Returns a formatted order list with the total price.'''
        res = self.view_list(self._item_list, 'order list')
        return res + f'\ntotal: {self.total_price}'
    
class OrderWithStatus:
    '''Represents a class of orders with states'''
    _status = valid.ValidString()

    def __init__(self) -> None:
        super().__init__()
        self._status = 'pending'
    
    def _check_access(self):
        '''Checks if the order is pending.'''
        if self._status == 'pending':
            return True
        return False
    
    def _cancel(self):
        '''Sets the status of the order to 'canceled'.'''
        self._status = 'canceled'

    def _close(self):
        '''Sets the status of the order to 'closed'.'''
        self._status = 'closed'


class PayableOrder(ABC):
    '''Represents a class of orders that must be paid.'''    
    _purchase = None

    def pay(self, salesperson = 'shop assistent'):
        '''Pays the order and closes it. Returns False if the order can't be paid; otherwise, returns the purchase.'''
        if not self._check_availability():
            return False
        result = self._make_purchase(salesperson)
        self._close()
        return result
        
    def _make_purchase(self,salesperson):
        '''Creates a purchase for the payable order and returns it.'''
        new_purchase = sm.Purchase(self.customer, salesperson, self, self.total_price, self.currency)
        self._purchase = new_purchase
        return new_purchase
    
    @abstractmethod
    def _check_availability(self):
        '''Checks if the order is open for payments.'''
        ...

        
class ManagebleOrder(OrderWithStatus, PayableOrder, ViewableOrder):
    def _check_availability(self):
        if self._check_access():
            return True
        raise ClosedOrderError
    

