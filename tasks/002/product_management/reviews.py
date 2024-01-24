import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import validations as valid
from abc import ABC, abstractmethod
import mixins.property_checker as pc

class Review:
    content=valid.ValidString()
    def __init__(self, customer, review) -> None:
        self.content = review
        self.customer = customer

class ItemWithReview:
    def __init__(self) -> None:
        super().__init__()
        self._reviews = []
        
    def add_review(self, customer, review):
        new_review = Review(customer, review)
        self._reviews.append(new_review)
    def view_reviews(self):
        res = ''
        for rev in self._reviews:
            res+=f'{rev.customer}: "{rev.content}"\n'
        if not res:
            return '0 left reviews'
        return res

class Reveiwer:
    def leave_review(self, product, review):
        product.add_review(self,review)
