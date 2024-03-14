import math
def paint_calc(height, width, cover):
  number_of_cans = (height * width) / cover

  cans_rounded = round(number_of_cans)
  print(f"You'll need {cans_rounded} cans of paint")


paint_calc(height=4, width=9, cover=5)


# print(math.ceil(4.2))
# #
# print(45%26)
# a = 10
# b = -1
# a *= b
# print(a)

some = 300 % 26
print(some)