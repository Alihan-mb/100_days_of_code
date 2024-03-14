def add(n1, n2):
    '''Сложение двух чисел'''
    return n1 + n2
def substract(n1, n2):
    '''Вычитание двух чисел'''
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": division
}
def calculator():
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    picking_the_operation = input("Pick an operation from the line above ")
    num2 = int(input("What's the second number?: "))
    calculations = operations[picking_the_operation]
    first_answer = round(calculations(num1, num2), 2)
    print(f"{num1} {picking_the_operation} {num2} = {first_answer}")

    should_continue = True
    while should_continue:
        yes_or_no = input("Would you like to continue? Type y or n ").lower()
        if yes_or_no == "y":
            picking_the_operation = input("Pick another operation ")
            calculations_two = operations[picking_the_operation]
            num3 = int(input("What's the next number? "))
            second_answer = calculations_two(first_answer, num3)
            print(f"{first_answer} {picking_the_operation} {num3} = {second_answer}")
            first_answer = second_answer
        else:
            should_continue = False
            print("starting_again")
            calculator()

calculator()