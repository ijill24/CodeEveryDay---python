# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 19:00:11 2020

@author: Jillian
"""
#I need to come back to this code because it's not working as intended.  Answering "N" does not direct to elif.

yesno = input("Would you like me to express your love to your valentine? Y or N ")
if yesno == "yes" or "Yes" or "Y" or "y":  
    name = input("Okay, great! What is your valentine's name? ")
    times = int(input("What is the magnitude of your love on a scale of 1-10? "))
    print(name + ", you are " + "s" + ("o " * times) + "loved" + ("!" * times))
elif yesno == "N" or "n" or "no" or "No":
    print("Maybe next year.")
else:
    print("That is not a valid response.")

