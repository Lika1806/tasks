import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from order_management.order_mixins import OrderWithStatus, ManagebleOrder
from order_management.order_types import OrderWithRepeatedItems


class Order(OrderWithRepeatedItems, ManagebleOrder, OrderWithStatus):
    @property
    def currency(self):
        return '$'




if __name__ == '__main__':
    order1 = Order('customer1')
    print(order1)
