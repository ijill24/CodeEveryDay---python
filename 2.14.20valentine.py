# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:00:11 2020

@author: Jillian
"""

yesno = input("Would you like me to express your love to your valentine? Y or N ")
if yesno.lower().startswith('y'):  
    name = input("Okay, great! What is your valentine's name? ")
    times = int(input("What is the magnitude of your love on a scale of 1-10? "))
    print(name + ", you are " + "s" + ("o " * times) + "loved" + ("!" * times))
elif yesno.lower().startswith('n'):
    print("Maybe next year.")
else:
    print("That is not a valid response.")

