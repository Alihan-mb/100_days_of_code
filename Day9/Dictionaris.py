programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop":"Action which is repetead over and over again",
  }
#Retriving data.txt from a dictionary
print(programming_dictionary["Loop"])

#Adding items to a dictionary
programming_dictionary["Mama"] = "A person who raises you."
print(programming_dictionary)

#Creating an empty dictionary
empty_dict = {}

#Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Editing an item
programming_dictionary["Bug"] = "a moth in your computer"
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])