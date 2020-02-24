# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:17:11 2020

@author: Jillian
"""
#Problem set 0 - MIT 60001
#Write a program that does the following in order: 
 
#1. Asks the user to enter a number “x” 
#2. Asks the user to enter a number “y”  
#3. Prints out number “x”, raised to the power “y”. 
#4. Prints out the log (base 2) of “x”.  

x=int(input("Enter a number."))
y=int(input("Enter a number."))
print(str(x) + "**" + str(y) + "=" + str(x**y))
import math
print(math.log(x,2))



