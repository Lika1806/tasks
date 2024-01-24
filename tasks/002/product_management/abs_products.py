import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import validations as valid
from abc import ABC, abstractmethod
from mixins.property_checker import SalaryCheckable, PropertyCheckable, NameCheckable
from product_management.rates import ItemWithRates
from product_management.reviews import ItemWithReview

class AbstractProduct(ABC):
    name = valid.ValidString()
    _price = valid.ValidNumber()
    description = valid.ValidString()
    def __init__(self, name, price, description) -> None:
        super().__init__()
        self.name = name
        self._price = price
        self.description = description


    def __str__(self):
        info = self.get_all_info()
        return (f'{self.view()}\n{info}\nrating: {self.rating:.2f}\ndescription: {self.description}\nreviews: {len(self._reviews)}\n')
 
    
    def view(self):
        return f'{self.name}:{self.price} AMD'
        
    @property
    def price(self):
        return self._price

    @abstractmethod
    def get_all_info(self):
        pass

class Product(AbstractProduct,ItemWithRates, ItemWithReview,PropertyCheckable, SalaryCheckable, NameCheckable):
    ...