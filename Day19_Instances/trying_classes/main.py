from class_for_water import Water
from creating_soda import Soda

water_aqua = Water("Aqua")
water_deneb = Water("Deneb")

water_aqua.minimal_bottle = 300
water_deneb.minimal_bottle = 500

aqua_bottle = water_aqua.checking_water_bottle_capacity(300)
deneb_bottle = water_deneb.checking_water_bottle_capacity(500)

soda_aqua = Soda(aqua_bottle)
soda_deneb = Soda(deneb_bottle)

cola_aqua = soda_aqua.creating_cola(4, 10, 0.5, 200)
cola_deneb = soda_deneb.creating_cola(3, 11, 0.7,170)
print(f"Price of Aqua Cola is {round(cola_aqua, 2)}$")
print(f"Price of Deneb Cola is {round(cola_deneb, 2)}$")

if cola_aqua < cola_deneb:
    print("Aqua Cola seems to be a better choice")
else:
    print("Go for Deneb Coa")