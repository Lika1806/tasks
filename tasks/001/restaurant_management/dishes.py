from restaurant_management.abs_dishes import *

class Drink(Dish, Pourable):
    dish_type = 'drink'

class HotDrink(Drink, Hot):
    def serve(self):
        self.heat()
        self.pour()
        print('serve in cup')

class ColdDrink(Drink, Cold):
    def serve(self):
        self.mix()
        self.pour()
        print('serve in glass')

class Appetizer(Dish, Cold):
    dish_type = 'appetizer'
    def serve(self):
        self.mix()
        print('serve in decorated plate')

class Soup(Dish, Cooked, Hot, Pourable):
    dish_type = 'soup'
    def serve(self):
        self.cook()
        self.heat()
        self.pour()
        print('serve in bowl')
    
class Pizza(Dish, Baked, Hot):
    dish_type = 'pizza'
    def serve(self):
        self.bake()
        self.heat()
        print('serve on wooden plate')

class Salad(Dish, Cold):
    dish_type = 'salad'
    def serve(self):
        self.mix()
        print('serve in decorated bowl')

class Desert(Dish, Baked):
    dish_type = 'desert'
    def serve(self):
        self.bake()
        print('serve on a plate')


if __name__ == '__main__':
    aperizer1 = Appetizer('tomato bruscetta', 1200)
    aperizer2 = Appetizer('olive bruscetta', 1400)
    soup1 = Soup('mushroom soup', 2000)
    pizza1 = Pizza('margarita', 1800)
    pizza2 = Pizza('pepperoni', 2100)
    salad1 = Salad('cesar', 1300)
    desert1 = Desert('cheesecake', 1500)
    dish_list = [aperizer1, aperizer2, soup1, pizza1,pizza2, salad1, desert1]
    desert1.serve()
    for item in dish_list:
        print(item)