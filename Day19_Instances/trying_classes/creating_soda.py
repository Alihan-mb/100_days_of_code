class Soda:
    def __init__(self, bottle_capacity):
        self.bottle_capacity = bottle_capacity

    def creating_cola(self, sugar, coffein, sparkling_water, price):
        cola = self.bottle_capacity + (sugar * coffein) + sparkling_water
        return cola / price