from Cryptodome.Util.RFC1751 import wordlist


def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(3, 5, 6))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model", "Toyota")
        self.color = kwargs.get("colour", "Blue")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", seats=4)

print(my_car.color)






