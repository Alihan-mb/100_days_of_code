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

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}
def is_resource_enough(order_ingridients):
    is_enough = True
    for item in order_ingridients:
        if order_ingridients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            is_enough = False

    return is_enough

def counting_coins(cost_of_drink):
    money_paid = 0
    while money_paid < cost_of_drink:
        money_inserted = input("Please, insert the money: Quarters, Dimes, Nickles, Pennies ").lower()
        if money_inserted == "quarters":
            money_paid += coins[money_inserted]
            print(f"${round(money_paid, 2)}")
        elif money_inserted == "dimes":
            money_paid += coins[money_inserted]
            print(f"${round(money_paid, 2)}")
        elif money_inserted == "nickles":
            money_paid += coins[money_inserted]
            print(f"${round(money_paid, 2)}")
        else:
            money_paid += coins[money_inserted]
            print(f"${round(money_paid, 2)}")
    return money_paid

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False



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
        drink_cost = MENU[choice]["cost"]
        profit = drink_cost
        if is_resource_enough(drink["ingredients"]):
            paid_amount = counting_coins(drink_cost)
            if paid_amount > drink_cost:
                is_transaction_successful()







