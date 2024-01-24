import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import validations as valid
from product_management.abs_products import Product

class Electronics(Product):
    def __init__(self, name, price, description, make, model) -> None:
        super().__init__(name, price, description)
        self.make = make
        self.model = model
        self.product_type = 'electronic'

    def get_all_info(self):
        return(f'category: electronics\nmake/model: {self.make} {self.model}')

class Clothing(Product):
    def __init__(self, name, price, description, brand, size) -> None:
        super().__init__(name, price, description)
        self.brand = brand
        self.size = size
        self.product_type = 'clothing'
        
    def get_all_info(self):
        return (f'category: clothing\nbrand: {self.brand}\nsize: {self.size}')

class Book(Product):
    def __init__(self, name, price, description, title, author) -> None:
        super().__init__(name, price, description)
        self.title = title
        self.author = author
        self.product_type = 'book'
    def get_all_info(self):
        return (f'category: books\ntitle: {self.title}\nauthor: {self.author}')

class Toys(Product):

    age_range = valid.ValidInteger()
    def __init__(self, name, price, description, brand,  age_range) -> None:
        super().__init__(name, price, description)
        self.brand = brand
        self.age_range = age_range
        self.product_type = 'toy'
    def get_all_info(self):
        return (f'category: toys\nbrand: {self.brand}\nage range: {self.age_range}+')
