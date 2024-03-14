from menu import MENU, resources
# Не выводить информацию про кофе, просто выводим репорт, когда пользователей выбирает кофе, мы туда вносим стоимость кофе, мы вычитаем из репорта ингредиенты кофе
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


def report():
    if "money" not in resources:
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        print(f"Resources in the machine:\n water: {water}\n milk: {milk} \n coffee: {coffee}")
    else:
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        money = resources["money"]
        print(
            f"Resources in the machine:\n water: {water}\n milk: {milk} \n coffee: {coffee}\n money: ${round(money, 2)}")



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
def change(cost_of_the_drink, money_inserted):
    if money_inserted > cost_of_the_drink:
        return money_inserted - cost_of_the_drink



off = True
while off:
    user_decision = input("Would you like (espresso/latte/cappuccino)? ").lower()
    if user_decision in ["espresso", "latte", "cappuccino"]:
        #check if machine has enough resources

        cost_of_drink = MENU[user_decision]["cost"]
        print(f"You picked {user_decision}, the price is {cost_of_drink}")
        money_paid = counting_coins(cost_of_drink)
        if money_paid > cost_of_drink:
            user_change = change(cost_of_drink, money_paid)
            resources["money"] = money_paid - user_change
            resources["water"] -= MENU[user_decision]["ingredients"]["water"]
            if user_decision != "espresso":
                resources["milk"] -= MENU[user_decision]["ingredients"]["milk"]
            resources["coffee"] -= MENU[user_decision]["ingredients"]["coffee"]
            print(f"Your change is {round(user_change, 2)}$")
        else:
            resources["money"] = cost_of_drink
            resources["water"] -= MENU[user_decision]["ingredients"]["water"]
            if user_decision != "espresso":
                resources["milk"] -= MENU[user_decision]["ingredients"]["milk"]
            resources["coffee"] -= MENU[user_decision]["ingredients"]["coffee"]

        print("Enjoy your coffee!")

    # HERE WE CHECK OTHER USER INPUT OPTIONS
    elif user_decision == "report":
        report()

    elif user_decision == "off":
        off = False

    else:
        print("I am sorry but that drink is not available, please choose between espresso, latte or cappuccino")
        user_decision = input("Would you like (espresso/latte/cappuccino)? ")
        print(f"You picked {user_decision}")
