class ItemGetterByID:
    def _get_item_by_id(self, _id, _list):
        for item in _list:
            if _id == item._id:
                return item
        
    def _get_item(self, item, _list):
        if isinstance(item, int):
            return self._get_item_by_id(item, _list)
        if item in _list:
            return item
        return None
     

    
class ItemGetterByIndex:
    def get_dish_by_index(self, _index):
        if _index <= len(self._dish_list):
            return self._dish_list[_index-1]
        else:
            return False
    def _check_item(self, item):
        if isinstance(item, int):
            item = self.get_dish_by_index(item)
        elif not item or item not in self._dish_list:
            raise ValueError('dish is not in menu')
        return item