#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

bill = float(input("Enter your bill, please\n"))
people_num = int(input("How many people are paying?\n"))
tip = input("How much of a tip you want to give? 10, 12, 15?")

tip_total = bill * float(tip) / 100.0
total_bill = bill + tip_total
total_topay = total_bill / people_num


print("Each person should pay: ${:.2f}".format(total_topay))