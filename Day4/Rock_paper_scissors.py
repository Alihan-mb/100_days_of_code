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
user_decision = input("Pick rock, paper or scissors\n").lower()
listing = [rock, paper, scissors]
abc = ["rock", "paper", "scissors"]
final_decision = abc.index(user_decision)
if final_decision >= 3 or final_decision < 0:
    print("Pick rock, paper or scissors")

if final_decision == 0:
    print(rock)
elif final_decision == 1:
    print(paper)
else:
    print(scissors)

pc_choice = random.choice(range(len(listing)))

if final_decision == 0 and pc_choice == 2:
    print(listing[pc_choice])
    print("User Won")

elif final_decision == 0 and pc_choice == 2:
    print(listing[pc_choice])
    print("User lost")

elif final_decision == pc_choice:
    print(listing[pc_choice])
    print("It's a draw")

elif final_decision == 0 and pc_choice == 1:
    print(listing[pc_choice])
    print("User Lost")

elif final_decision == 1 and pc_choice == 2:
    print(listing[pc_choice])
    print("User Lost")

elif final_decision == 2 and pc_choice == 0:
    print(listing[pc_choice])
    print("User Lost")

else:
    print(listing[pc_choice])
    print("User won!")