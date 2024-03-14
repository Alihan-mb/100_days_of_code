import random
from my_module import pi

random_integer = random.randint(1, 100)
print(random_integer)

print(pi)

random_floating = random.random()
print(round(random_floating, 2))

random_to_five = random.uniform(1, 5)
print(round(random_to_five, 2))


list = ["tr", "bb", "mm"]
ran = random.choice(range(len(list)))
print(ran ,list[ran])
mama = list[ran]
if ran == 0:
    print("hi")
elif ran == 1:
    print("FF")
else:
    print("CC")