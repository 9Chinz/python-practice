class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water" : water,
            "milk" : milk,
            "coffee" : coffee
        }


class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name = "latte(25)", water = 200, milk = 150, coffee = 24, cost = 25),
            MenuItem(name = "espresso(15)", water = 50, milk = 0, coffee = 18, cost = 15),
            MenuItem(name = "cappuccino(30)", water = 250, milk = 100, coffee = 24, cost = 25),
        ]
    
    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    
    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available. ")