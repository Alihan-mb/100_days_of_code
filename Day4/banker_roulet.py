names_string = input("How many people are willing to pay")
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
len_names = len(names)
random_int = random.randint(0, len_names-1)
final_name = names[random_int]
print(f"{final_name} is going to buy the meal today!")
