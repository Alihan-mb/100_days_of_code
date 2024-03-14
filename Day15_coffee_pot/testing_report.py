import menu as machine

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}


def drink_requirements(drink):
    if drink == "report":
        if "money" not in machine.resources:
            water_res = machine.resources["water"]
            milk_res = machine.resources["milk"]
            coffee_res = machine.resources["coffee"]
            print(f"Resources in the machine:\n water: {water_res}\n milk: {milk_res} \n coffee: {coffee_res}")
        else:
            water_res = machine.resources["water"]
            milk_res = machine.resources["milk"]
            coffee_res = machine.resources["coffee"]
            money_res = machine.resources["money"]
            print(
                f"Resources in the machine:\n water: {water_res}\n milk: {milk_res} \n coffee: {coffee_res}\n money: ${round(money_res, 2)}")
    elif drink == "espresso":
        water = machine.MENU[drink]["ingredients"]["water"]
        coffee = machine.MENU[drink]["ingredients"]["coffee"]
        cost = machine.MENU[drink]["cost"]

        print(f"ingredients are\n water: {water}\n coffee: {coffee};\n\nthe cost is: {cost}")

    elif drink == "latte" or drink == "cappuccino":
        water = machine.MENU[drink]["ingredients"]["water"]
        milk = machine.MENU[drink]["ingredients"]["milk"]
        coffee = machine.MENU[drink]["ingredients"]["coffee"]
        cost = machine.MENU[drink]["cost"]
        print(f"ingredients are:\n water: {water}\n milk: {milk} \n coffee: {coffee};\nthe cost is: {cost}")


# def report():
#     if "money" not in machine.resources:
#         water = machine.resources["water"]
#         milk = machine.resources["milk"]
#         coffee = machine.resources["coffee"]
#         print(f"Resources in the machine:\n water: {water}\n milk: {milk} \n coffee: {coffee}")
#     else:
#         water = machine.resources["water"]
#         milk = machine.resources["milk"]
#         coffee = machine.resources["coffee"]
#         money = machine.resources["money"]
#         print(
#             f"Resources in the machine:\n water: {water}\n milk: {milk} \n coffee: {coffee}\n money: ${round(money, 2)}")



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
        print(f"You picked {user_decision}")
        cost_of_drink = drink_requirements(user_decision)
        print(cost_of_drink)
        money_paid = counting_coins(cost_of_drink)

        if money_paid > cost_of_drink:
            user_change = change(cost_of_drink, money_paid)
            machine.resources["money"] = money_paid - user_change
            print(f"Your change is {round(user_change, 2)}$")
        else:
            machine.resources["money"] = cost_of_drink

        print("Enjoy your coffee!")

    # HERE WE CHECK OTHER USER INPUT OPTIONS
    elif user_decision == "report":
        drink_requirements(user_decision)
        user_decision = input("Would you like (espresso/latte/cappuccino)? ").lower()
        cost_of_drink = drink_requirements(user_decision)

    elif user_decision == "off":
        off = False

    else:
        print("I am sorry but that drink is not available, please choose between espresso, latte or cappuccino")
        user_decision = input("Would you like (espresso/latte/cappuccino)? ")
        print(f"You picked {user_decision}")
        cost_of_drink = drink_requirements(user_decision)