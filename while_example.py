
# you have three lives. if I roll 6, you win.
# If not a 6, you lose 1 life

from random import randint

lives = 3
while lives: #To keep the game playing by itslef until win, change it for "while True: "
    roll = randint(1, 6) #make sure to not put "a:" and "b:" !!
    if roll == 6:
        print("You rolled a 6! You win!")
        break #This exits the while even if lives still > 0
    #there is no other way to get here, unless I did not roll a 6
    print(f"You rolled a {roll}! You lose a life")
    lives -= 1
    print(f"Lives left: {lives}")

else: #else from while!!
    print("You lost!")
