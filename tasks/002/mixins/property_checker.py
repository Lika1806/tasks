class PropertyCheckable:
    def _check_property(self, key, value):
        if value is None:
            return True
        if self.__dict__.get(key) == value:
            return True
        return False
    
    def _check_text(self, key, value):
        if value is None:
            return True
        if value in self.__dict__.get(key):
            return True
        return False
    
    def check_properties(self, property_list):
        res = True
        for name, value in property_list.items():
            res = res and self._check_property(name, value) 
        return res
    
    def check_properties_text(self, property_list):
        res = True
        for name, value in property_list.items():
            res = res and self._check_text(name, value) 
        return res

class NameCheckable:
    def check_name(self, name):
        if not name or name in self.name:
            return True
        return False
    
class SalaryCheckable:
    def check_salary(self, min_salary, max_salary):
        res = True
        if max_salary:
            res = self.price <= max_salary
        return res and self.price >= min_salary

