from microbit import *
import random


while True:
    x = 2
    y = 4
    random_y = 4

    if button_a.get_presses():
        if x > 0:
            x -= 1
    elif button_b.get_presses():
        if x < 4:
            x += 1
    display.clear()
    display.set_pixel(x,y,9)
    sleep(100)  
    r = random.randint(1, 5)
    
    if r == 0:
        if random_y < 0:
            y -= 1
        display.set_pixel(0, random_y, 9)
        
    elif r == 1:
        if random_y < 0:
            y -= 1
        display.set_pixel(1, random_y, 9)
        
    elif r == 2:
        if random_y < 0:
            y -= 1
        display.set_pixel(2, random_y, 9)
        
    elif r == 3:
        if random_y < 0:
            y -= 1
        display.set_pixel(3, random_y, 9)
        
        
    elif r == 4:
        if random_y < 0:
            y -= 1
        display.set_pixel(4, random_y, 9)
        
    display.clear()


    
    