import random
number_to_guess = random.randint(1, 100)

if input("Pick the mode, easy or hard: ").lower() == "easy":
  attempts = 10
  print(f"You have {attempts} attempts")
else:
  attempts = 5
  print(f"You have {attempts} attempts")

while attempts > 0:
  def guesser(number):
    if number <  number_to_guess:
      return "Too low, guess higher"
    elif number > number_to_guess:
      return "Too high, guess lower"
    else:
      return "That's it, you won!"

  user_number = int(input("Guess any number between 1 and 100 "))
  result = guesser(user_number)
  if result != "That's it, you won!":
    attempts -= 1
    if attempts != 0:
      print(f"Number of attempts left = {attempts}")
      print(result)
    else:
      print("You ran out of attempts")
      print(f"Number to guess was {number_to_guess}")
  else:
    print(result)
    attempts = 0