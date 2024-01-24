import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import product_management.product_types as products
import customer as client
from order_management.general_orders import Order
from test_functions import Test, print_result


def test():
    with Test('creating customers'):
        customer1 = client.Customer('Anna', '+37477889900', 'aaa@gmail.com')
        customer2 = client.Customer('Bob', '+37488889900', 'bbb@gmail.com', 60000)
        customer3 = client.Customer('Charles', '+37488889911', 'ccc@gmail.com', 120000)
        customer4 = client.Customer('David', '+37488889922', 'ddd@gmail.com', 10000)
        customers = [customer1,customer2, customer3, customer4]
        for customer in customers:
            print_result(customer)    

    with Test('adding money to balace'):
        customer1.increase_budget(120000)
        customer4.increase_budget(60000)

    with Test('Viewing customers'):
        print(customer1.view())
        print(customer2.view())
        print(customer3.view())
        print(customer4.view())

    with Test('creating products'):
        samsung_galaxy = products.Electronics('phone-samsung galaxy', 120*400, ' budget-friendly option with decent specs', 'samsung', 'galaxy A12')
        xiomi_redmi = products.Electronics('phone-xiomi redmi note', 250*400, 'good performance at an affordable price', 'xiomi', 'redmi note10')
        iphone = products.Electronics('phone-iphone', 1100*400, 'known for its powerful performance and impressive cameras', 'apple', '13 pro max')
        t_shirt1 = products.Clothing('happy t-shirt', 25*400, 'a summer t-shirt', 'prada', 28)
        book1 = products.Book('book name', 10*400, 'book about something', 'the title', 'very good person')
        toy1 = products.Toys('toy name', 15*400, 'toy for kids and adults', 'Barbie', 3)
        all_products = [samsung_galaxy,xiomi_redmi, iphone, t_shirt1, book1, toy1]

        for product_ in all_products:
            print_result(product_)

    with Test('making order'):
        customer1.creat_order(samsung_galaxy, book1)
        customer1.creat_order(toy1,t_shirt1)
        customer1.creat_order(*all_products)
        customer1.creat_order(t_shirt1, book1,toy1)

    with Test('viewing orders'):
        for item in customer1.get_order_list():
            print(item)
    

    with Test('viewing order'):
        print(customer1.view_order(3))

    with Test('leaving review'):
        customer1.leave_review(samsung_galaxy, 'I liked the product')
        customer2.leave_review(samsung_galaxy, 'the phone is ok')
        customer3.leave_review(samsung_galaxy, 'the quality is fantastic')
        customer4.leave_review(samsung_galaxy, 'will buy another one')

    with Test('viewing reviews'):
        print(samsung_galaxy.view_reviews())
    
    with Test('rating product'):
        customer1.rate(samsung_galaxy, 5)
        customer2.rate(samsung_galaxy,9)
        customer3.rate(samsung_galaxy,2)
        customer4.rate(samsung_galaxy, 10)
    
    with Test('viewing product'):
        print(samsung_galaxy)

    with Test('paying order'):
        customer1.pay(2)
        print_result(customer1.view_orders())
        print_result(customer1.view_purchase_history())

    with Test('tying to pay order with higher price then budget', expect_error=True):
        customer1.pay(3)

    with Test('canceling order'):
        customer1.cancel_order(3)
        print_result(customer1.view_orders())

    with Test('removing from order'):
        customer1.remove_from_order(1, samsung_galaxy)
        print_result(customer1.view_order(1))
    with Test('removing last element from order'):        
        customer1.remove_from_order(1, book1)
        print_result(customer1.view_order(1))
    with Test('removing not existing item', expect_error=True):
        customer1.remove_from_order(4,samsung_galaxy)


    with Test('seraching item'):
        customer1.search(all_products, name = 'phone', make = 'xiomi', min_price=1000, display=True)
        customer1.search(all_products, description = 'a', min_price=1000, display=True)
    return


        
if __name__ == '__main__':
    test()