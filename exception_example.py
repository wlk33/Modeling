
#Handling exceptions

name = input("what is your name? ")
#lets write this in a simpler way
age2 = input(f"How old are you {name}? ")
try:
    age2 = int(age2) #Here there can be a problem
    print(f"{name}, you were born in {2024-age2}")
    #7/0
except ValueError:
    print("Please enter a valid value for age")
    print("I can also print this in case of error that I prevented")
except ZeroDivisionError:
    print("you can't divide by 0!")
except:
    print("this is another type of error")
else: # this is for no exception
    print("Thank you for playing as expected")
finally: #this will be executed no matter what, at the very end
    print("Thanks for playing the game")
