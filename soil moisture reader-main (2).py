# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
reading=0
happy = Image.HAPPY
sad = Image.SAD
while True:
    reading = pin0.read_analog()
    if (reading < 600):
        display.show(sad)
        display.scroll('water me!')
        sleep(10000)
    else:
        display.show(happy)
