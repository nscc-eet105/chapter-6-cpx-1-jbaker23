# Write your code here :-)
# This is Jacob Baker and this is Chapter 6 CPX 1 whihc I am completing on June 30
from adafruit_circuitplayground import cp
import time
import random
pattern = (2, 4, 1, 8, 3, 5, 7, 9, 6)
black = (0, 0, 0)
def pixel_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

while True:
    for index in pattern:
        color = pixel_color()
        cp.pixels[index] = color
        time.sleep(0.5)
        cp.pixels[index] = black
