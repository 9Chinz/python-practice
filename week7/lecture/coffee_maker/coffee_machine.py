MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_enough_resource(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            return False
    return True

def process_coin():
    total = 0
    print("Insert coins")
    baht = int(input("How many 1 baht coin: "))
    total += baht
    baht5= int(input("How many 5 baht coin: "))
    total += baht5 * 5
    baht10 = int(input("How many 10 baht coin: "))
    total += baht10 * 10
    return total

def is_transaction_successul(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Refund!")
        return False

def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here's your coffee {drink_name}")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/Capuchino): ")

    if choice.lower() == "off":
        print("Turning off")
        is_on = False
    elif choice.lower() == "report":
        print(f"water {resources['water']} ml")
        print(f"milk {resources['milk']} ml")
        print(f"coffee {resources['coffee']} ml")
        print(f"profit {profit} baht")
    else:
        drink_choice = MENU[choice]
        if is_enough_resource(drink_choice['ingredients']):
            payment = process_coin()
            if is_transaction_successul(payment, drink_choice['cost']):
                make_coffee(choice, drink_choice['ingredients'])
