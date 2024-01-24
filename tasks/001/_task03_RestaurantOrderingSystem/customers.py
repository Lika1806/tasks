import order_management.general_clients as client

class Client(client.Client):
    def view_menu(self, menu):
        return menu.view_menu()
    
    def remove_from_order(self, order, *items, menu=None):
        if menu:
            items = menu._get_dish_list(items)
        return super().remove_from_order(order, *items)