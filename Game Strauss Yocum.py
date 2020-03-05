from gpiozero import Button
from sense_hat import SenseHat 
import random

Button3 = Button(27)        
Button1 = Button(6)
Button2 = Button(17)
           
sense = SenseHat()
    
b = [0, 0, 0]
g = [0, 255, 0]
        
        
one = [
b,b,b,b,b,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
]
        
two = [
b,b,b,b,b,b,b,b,
b,b,b,g,g,b,b,b,
b,b,g,b,b,g,b,b,
b,b,b,b,g,b,b,b,
b,b,b,g,b,b,b,b,
b,b,g,g,g,g,b,b,
b,b,b,b,b,b,b,b,
b,b,b,b,b,b,b,b,
]
        
three = [
b,b,b,b,b,b,b,b,
b,b,b,g,g,b,b,b,
b,b,g,b,b,g,b,b,
b,b,b,b,b,g,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,g,b,b,
b,b,g,b,b,g,b,b,
b,b,b,g,g,b,b,b,
]
            
four = [
b,b,b,b,b,b,b,b,
b,b,g,b,b,g,b,b,
b,b,g,b,b,g,b,b,
b,b,g,g,g,g,g,b,
b,b,b,b,b,g,b,b,
b,b,b,b,b,g,b,b,
b,b,b,b,b,g,b,b,
b,b,b,b,b,b,b,b,
]

five = [
b,b,b,b,b,b,b,b,
b,b,g,g,g,g,b,b,
b,b,g,b,b,b,b,b,
b,b,g,g,g,b,b,b,
b,b,b,b,b,g,b,b,
b,b,g,b,b,g,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
]
        
six = [
b,b,b,b,b,b,b,b,
b,b,b,g,b,b,b,b,
b,b,g,b,b,b,b,b,
b,b,g,b,b,b,b,b,
b,b,g,g,g,b,b,b,
b,b,g,b,b,g,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
]
        
seven = [
b,b,b,b,b,b,b,b,
b,b,g,g,g,g,b,b,
b,b,b,b,b,g,b,b,
b,b,b,b,b,g,b,b,
b,b,b,b,b,g,b,b,
b,b,b,b,b,g,b,b,
b,b,b,b,b,g,b,b,
b,b,b,b,b,b,b,b,
]
        
eight = [
b,b,b,g,g,b,b,b,
b,b,g,b,b,g,b,b,
b,b,g,b,b,g,b,b,
b,b,b,g,g,b,b,b,
b,b,g,b,b,g,b,b,
b,b,g,b,b,g,b,b,
b,b,b,g,g,b,b,b,
b,b,b,b,b,b,b,b,
]
        
nine = [
b,b,b,b,b,b,b,b,
b,b,g,g,g,g,b,b,
b,b,g,b,b,g,b,b,
b,b,g,g,g,g,b,b,
b,b,b,b,b,g,b,b,
b,b,b,b,b,g,b,b,
b,b,b,b,b,g,b,b,
b,b,b,b,b,b,b,b,
]
        
ten = [
b,b,b,b,b,b,b,b,
b,g,b,g,g,g,g,b,
b,g,b,g,b,b,g,b,
b,g,b,g,b,b,g,b,
b,g,b,g,b,b,g,b,
b,g,b,g,b,b,g,b,
b,g,b,g,g,g,g,b,
b,b,b,b,b,b,b,b,
]

while True: 
    if Button3.is_pressed()
               random_number = random.randint(1,10)
               if random_number == (1):
                   sense.set_pixels(one)
               elif random_number == (2):
                   sense.set_pixels(two)
               elif random_number == (3):
                   sense.set_pixels(three)
               elif random_number == (4):
                   sense.set_pixels(four)
               elif random_number == (5):
                   sense.set_pixels(five)
               elif random_number == (6):
                   sense.set_pixels(six)
               elif random_number == (7):
                   sense.set_pixels(seven)
               elif random_number == (8):
                   sense.set_pixels(eight)
               elif random_number == (9):
                   sense.set_pixels(nine)
               elif random_number == (10):
                   sense.set_pixels(ten)
       

    if Button1.is_pressed:
           print("Player 1 wins!")
            
    if Button2.is_pressed:
           print("Player 2 wins!")    
            
