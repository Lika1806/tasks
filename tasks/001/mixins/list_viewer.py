class ListViewer:
    def view_list(self, list_, list_name, enumerated = False):
        if not list_:
            return f'{list_name} is empty'
        if isinstance(list_, dict):
            return self.__view_dict(list_)
        if enumerated:
            return  self.__view_enumerated_list(list_)
        return self.__view_flat_list(list_)
    
    def __view_flat_list(self, list_) -> str:
        res = ''
        for item in list_:
            res += f'{item.view()}\n'
        return res
    
    def __view_enumerated_list(self, list_) -> str:
        res = ''
        for number, item in enumerate(list_, 1):
            res += f'{number}: {item.view()}\n'
        return res
    
    def __view_dict(self, list_):
        res = ''
        for item ,count in list_.items():
            res += f'{item.view()}: x{count}\n'
        return res
