import validations as valid
from abc import ABC, abstractmethod

class Person(ABC):
    '''represents a class of general person'''
    role = valid.ValidString()
    name = valid.ValidString()
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name  

    def view(self) -> str:
        '''returns a long description of an instance'''
        return f"{self.role}\nname: {self.name}\n"  
    
    @abstractmethod
    def __str__(self):
        '''returns a short description of an instance'''
        pass

class PersonWithConacts(Person):
    '''represents a class of person with contact informations: phone number, email'''
    phone = valid.ValidPhoneNumber()
    email = valid.ValidEmail()
    def __init__(self, name: str, phone: str, email: str) -> None:
        super().__init__(name)
        self.phone = phone
        self.email = email

    def view(self) -> str:
        '''returns a long description of an instance'''
        res = super().view()
        return res + f"phone number: {self.phone}\nemail: {self.email}\n"  


