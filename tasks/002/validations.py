import re
from typing import Any
from datetime import datetime
from abc import ABC, abstractmethod

class ValidAbs(ABC):
    def __set_name__(self, instance, name):
        self.property_name = name
    
    @abstractmethod
    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name) 

class ValidDate(ValidAbs):
    def __set__(self, instance, date):
        if not isinstance(date, str):
            raise ValueError('Value must be string')
        try:
            new_time = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError('date format is invalid')
        instance.__dict__[self.property_name] = new_time
    
    def __get__(self,instance, owner_class):
        if instance is None:
            return None
        time = instance.__dict__.get(self.property_name)
        if time:
            time = time.strftime('%Y-%m-%d')
        return time     

class ValidTime(ValidAbs):
    def __set__(self, instance, time):
        if not isinstance(time, str):
            raise ValueError('Value must be string')
        try:
            new_time = datetime.strptime(time, '%H:%M')
        except ValueError:
            raise ValueError('time format is invalid')
        instance.__dict__[self.property_name] = new_time
       
    def __get__(self, instance, owner_class):
        if instance is None:
            return None
        time = instance.__dict__.get(self.property_name)
        if time:
            time = time.strftime('%I:%M %p')
        return time     
            
class ValidEmail(ValidAbs):
    def __set__(self, instance, email):
        if not isinstance(email, str):
            raise ValueError('Value must be string')
        if email == '':
            raise ValueError('Input string can\'t be empty')
        regex = r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(regex, email):
            raise ValueError('email is invalid')
        instance.__dict__[self.property_name] = email


class ValidString(ValidAbs):
    def __set__(self, instance, name):
        if not isinstance(name, str):
            raise ValueError('Value must be string')
        if name == '':
            raise ValueError('Input string can\'t be empty')
        instance.__dict__[self.property_name] = name



class ValidPhoneNumber(ValidAbs):
    def __set__(self, instance, value):
        pattern1 = '^\\+374[0-9]{8}$'
        pattern2 = '^[0-9]{9}$'
        if not re.fullmatch(pattern1, value) and not re.match(pattern2, value):
            raise ValueError("Phone number invalid")
        instance.__dict__[self.property_name] = value



class ValidNumber(ValidAbs):
    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value invalid")
        instance.__dict__[self.property_name] = value


       

class ValidInteger(ValidAbs):
 
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Value invalid")
        instance.__dict__[self.property_name] = value


  

class ValidCurrency(ValidAbs):
 
    def __set__(self, instance, value):
        value_list = {'$', 'USD', 'AMD', 'RUB'}
        if value not in value_list:
            raise ValueError("Value is invalid")
        instance.__dict__[self.property_name] = value


  
class ValidUsername(ValidAbs):
    def __set__(self, instance, value):
        res_words = {'admin', 'root'}
        if value.lower() in res_words or not 5<=len(value)<=20 or not value.isalnum():
            raise ValueError("Username is invalid")
        instance.__dict__[self.property_name] = value

class ValidPassword(ValidAbs):
    def __set__(self, instance, value):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#+=_*%])[a-zA-Z0-9!+-_@#*%]{8,30}$'

        if not re.fullmatch(pattern, value):
                raise ValueError("Password is invalid")
        instance.__dict__[self.property_name] = value
