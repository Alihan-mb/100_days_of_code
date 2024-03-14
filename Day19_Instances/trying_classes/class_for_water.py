class Water:
    def __init__(self, water_name):
        self.water = water_name
        self.minimal_bottle = 0


    def checking_water_bottle_capacity(self, bottle_minimal_capacity):
        conteiner = bottle_minimal_capacity + self.minimal_bottle
        return conteiner


