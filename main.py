
import random
import China, austria
from austria import cook as austria_cook
from China import cook as China_cook
from latam.argentina import cook as argentina_cook
from latam.brazil import cook as brazil_cook
from latam.mexico.yucatan import cook as yucatan_cook

def cook():
    print("We are making Paella")

print("Random number is: ", random.randint(1, 10))
China.cook()
China.greet()
cook()
austria.cook()
austria.greet()
China_cook()
austria_cook()
cook()
argentina_cook()
brazil_cook()
yucatan_cook()
