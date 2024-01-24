from abc import abstractmethod, ABC

class SearcherByProperty:
    def _search_properties(self, item_list, property_list):
        res = []
        for item in item_list:
            if item.check_properties(property_list):
                    res.append(item)
        return res


class ItemSearcher(ABC):

    def _search(self, item_list, *, text_property_list = [],value_property_list=[], min_salary = 0, max_salary = None):
        res = []
        for item in item_list:
            if (item.check_properties(value_property_list) and 
                item.check_properties_text(text_property_list) and
                item.check_salary(min_salary = min_salary,max_salary=max_salary)):
                    res.append(item)
        return res

    @abstractmethod
    def search(*args, **kwargs):
         ...