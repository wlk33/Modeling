
# Let's create a virtual bartender that serves you if you are of legal age

from random import choice

drinks = ["whiskey", "rum", "tequila", "gin", "sake", "wine", "beer", "vodka"]
mixers = ["fanta limon", "fanta", "red bull", "tonic", "cola", "soda"]

#print(f"{choice(drinks)} {choice(mixers)}")
print("I am the virtual bartender, welcome to my humble bar")
name = input("How should I call you? ")

try:
   age = input("How old are you? ")
   age = int(age) # this is where we can have problems
   legal = None
   country = input("Where are you from? ")
   if age < 14:
       legal = False
   elif age < 16:
       if country == "Austria":
           legal = True
       else:
           legal = False
   elif age < 18:
       if country == "Austria" or country == "Luxembourg":
           legal = True
       else:
           legal = False
   elif age < 21:
       if country == "USA" or country == "UAE":
           legal = False
       else:
           legal = True
   else: # for age greater than 21
       legal = True
   if legal:
       print(f"Here is a {choice(drinks)} {choice(mixers)}")
   else:
       print(f"I can only serve you {choice(mixers)}")


except ValueError:
    print("I don't have time for your games! Get out!")
