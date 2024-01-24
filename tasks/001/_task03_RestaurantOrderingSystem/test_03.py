import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_functions import Test, print_result
import task03_RestaurantOrderingSystem.menus as menus
import task03_RestaurantOrderingSystem.customers as client
import restaurant_management.dishes as dish

def test():
    with Test('creating customers'):
        customer1 = client.Client('Anna', '+37477889900', 'aaa@gmail.com')
        customer2 = client.Client('Bob', '+37488889900', 'bbb@gmail.com', 60000)
        customer3 = client.Client('Charles', '+37488889911', 'ccc@gmail.com', 120000)
        customer4 = client.Client('David', '+37488889922', 'ddd@gmail.com', 10000)
        customers = [customer1,customer2, customer3, customer4]
        for customer in customers:
            print_result(customer)    

    with Test('adding money to balace'):
        customer1.increase_budget(20000)
        customer4.increase_budget(60000)

    with Test('Viewing customers'):
        print(customer1.view())
        print(customer2.view())
        print(customer3.view())
        print(customer4.view())

    with Test('creating dishes'):
        aperizer1 = dish.Appetizer('tomato bruscetta', 1200)
        aperizer2 = dish.Appetizer('olive bruscetta', 1400)
        soup1 = dish.Soup('mushroom soup', 2000)
        pizza1 = dish.Pizza('margarita', 1800)
        pizza2 = dish.Pizza('pepperoni', 2100)
        salad1 = dish.Salad('cesar', 1300)
        desert1 = dish.Desert('cheesecake', 1500)
        very_expensive_dish = dish.Desert('something', 120000)
        dishes = [aperizer1, aperizer2, soup1, pizza1,pizza2, salad1, desert1, very_expensive_dish]

        for dish_ in dishes:
            print_result(dish_)

    with Test('creating menu and viewing it'):
        menu1 = menus.Menu(*dishes)
        print_result(menu1.view_menu())

    with Test('making order'):
        customer1.creat_order(soup1, pizza1)
        order2 = customer1.creat_order(pizza2, desert1, salad1, aperizer1)
        customer1.creat_order(desert1, pizza1, pizza1, salad1)
        print_result(customer1.view_order(1))
        print_result(customer1.view_order(3))
        menu1.creat_order(customer1, 4,5,8)
        print_result(customer1.view_order(4))
    with Test('printing all orders'):
        print(customer1.view_orders())

    with Test('paying order'):
        customer1.pay(1)
        print_result(customer1.view_orders())
        print_result(customer1.view_purchase_history())

    with Test('tying to pay order with higher price then budget', expect_error=True):
        customer1.pay(4)
        print_result(customer1.view_purchase_history())

    with Test('viewing removed order', expect_error=True):

        print_result(customer1.view_order(1))

    with Test('removing from order'):
        customer1.remove_from_order(4, 8, menu=menu1)
        print_result(customer1.view_order(4))
    return

if __name__ == '__main__':
    test()
