print("The Love Calculator is calculating your score...")
name1 = input("What is your name?") # What is your name?
name2 = input("What is their name?") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

letter = "True"
count = name1.count(letter)
if count > 5:
    print("The letter 'l' appears more than 5 times in the string.")
else:
    print("The letter 'l' appears 5 or fewer times in the string.")



# You are going to write a program that tests the compatibility between two people.
#
# To work out the love score between two people:
#
# Take both people's names and check for the number of times the letters in the word TRUE occurs.
#
# Then check for the number of times the letters in the word LOVE occurs.
#
# Then combine these numbers to make a 2 digit number.
#
# For Love Scores less than 10 or greater than 90, the message should be:
#
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
#
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:
#
# "Your score is *z*."