MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_enough(order_ingridients):
    '''Return True when order can be made and returns false when resources are not enough'''
    is_enough = True
    for item in order_ingridients:
        if order_ingridients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            is_enough = False

    return is_enough

def is_transaction_success(money_received, drink_cost):
    '''Return True when the payment is accepted or False if the money is'''
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False

def process_coins():
    '''Returns the total calculated from coins inserted'''
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def make_coffee(drink_name, order_ingr):
    for item in order_ingr:
        resources[item] -= order_ingr[item]
    print(f"Here is your {drink_name}")

is_on = True

while is_on:
    choice = input("What would you like? Espresso, Latte, Cappuccino ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
       print(f"Water: {resources['water']}ml")
       print(f"Milk: {resources['milk']}ml")
       print(f"Coffee: {resources['coffee']}g")
       print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_enough(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_success(money_received=payment, drink_cost=drink["cost"]):
                make_coffee(choice, drink["ingredients"])




