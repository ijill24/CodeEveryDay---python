#Guess my number game

import random
import time
random.seed(time.perf_counter())
x = random.randint(1, 100)
while True:
    i =int(input('Guess a number between 0-100.'))
    if i < x:
        print('Too low. Guess again!')
    elif i > x:
        print('Too high. Guess again!')
    else:
        print('You got it!')
        break
