############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards_of_pc = []
cards_of_player = []
total_of_player = 0
total_of_pc = 0
def first_draw(num, playing_or_not):
  '''Тут мы раздаем первые карты'''
  if playing_or_not == "y":
    while num < 2:
      num +=1
      random_card_player = random.choice(cards)
      random_card_pc = random.choice(cards)
      cards_of_pc.append(random_card_pc)
      cards_of_player.append(random_card_player)
    counting_cards()
  else:
    print("Why did you launch the game then? ")


def counting_cards():
  '''Тут мы считаем карты'''
  global total_of_player
  global total_of_pc
  total_of_player = sum(cards_of_player)
  total_of_pc = sum(cards_of_pc)
  print(f"DEALER CARDS {cards_of_pc[0]}, PLAYER CARDS {cards_of_player}, TOTAL PLAYER SCORE {total_of_player}")
  going_again_or_not()
def going_again_or_not():
  '''Раздаем карты заново или нет'''
  stop_or_go = input("Type y to get another card, type n to pass ").lower()
  if stop_or_go == "y":
    new_card_player = random.choice(cards)
    new_card_pc = random.choice(cards)
    cards_of_pc.append(new_card_player)
    cards_of_player.append(new_card_pc)
    total_of_player = sum(cards_of_player)
    total_of_pc = sum(cards_of_pc)
    if total_of_player >= 22:
      if 11 in cards_of_player and len(cards_of_player) == 2:
        cards_of_player.remove(11)
        cards_of_player.append(1)
      else:
        print(f"Your hand {cards_of_player}, final score {total_of_player}")
        print(f"PC hand is {cards_of_pc}, final score {total_of_pc}")
        print("Bust! You lost!")
    elif total_of_pc >= 22:
      if 11 in cards_of_pc and len(cards_of_pc) == 2:
        cards_of_pc.remove(11)
        cards_of_pc.append(1)
      else:
        print(f"Your hand {cards_of_player}, final score {total_of_player}")
        print(f"PC hand is {cards_of_pc}, final score {total_of_pc}")
        print("You win! PC went over 21")
    else:
      print(f"DEALER CARDS {cards_of_pc[0]}, PLAYER CARDS {cards_of_player}, TOTAL PLAYER SCORE {total_of_player}")
      stop_or_go = input("Type y to get another card, type n to pass ").lower()
    if stop_or_go == "y":
      going_again_or_not()
  else:
      counting()
def counting():
    '''подсчет результатов'''
    if total_of_player > total_of_pc:
      print(f"Your hand {cards_of_player}, final score {total_of_player}")
      print(f"PC hand is {cards_of_pc}, final score {total_of_pc}")
      print("You win!")
    elif total_of_player < total_of_pc:
      print(f"Your hand {cards_of_player}, final score {total_of_player}")
      print(f"PC hand is {cards_of_pc}, final score {total_of_pc}")
      print("You lost!")
    else:
      print(f"Your hand {cards_of_player}, final score {total_of_player}")
      print(f"PC hand is {cards_of_pc}, final score {total_of_pc}")
      print("It's a draw!")


play_or_not = input("Do you want to playe a game of BlackJack? Type Y if yes, N of not ").lower()
first_draw(0, playing_or_not=play_or_not)