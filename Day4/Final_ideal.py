import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_choice = int(input("Type 0 for rock,1 paper or 2 scissors\n"))
listing = [rock, paper, scissors]

if user_choice >= 3 or user_choice < 0:
    print("You had to pick 1, 2 or 3. YOU LOST")
else:
    print("User chose:")
    print(listing[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(listing[computer_choice])

    if user_choice == 0 and computer_choice == 2:
      print("You win!")
    elif computer_choice == 0 and user_choice == 2:
      print("You lose")
    elif computer_choice > user_choice:
      print("You lose")
    elif user_choice > computer_choice:
      print("You win!")
    elif computer_choice == user_choice:
      print("It's a draw")
