enemies = 1
def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

game_level = 3
def create_enemy():
  enemies = ["Skeleton", "Zombie", "Alien"]
  if game_level < 5:
    new_enemy = enemies[0]

  print(new_enemy)


i = 50
def foo():
  i = 100
  return i


new_i = foo()
print(i)
print(new_i)