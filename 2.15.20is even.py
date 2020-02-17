# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:19:46 2020

@author: Jillian
"""

def is_even(i):
    """
    input: i, a positive integer
    Returns True if i is even, otherwise False
    """
    remainder = i % 2
    return remainder == 0

print ("All numbers between 0 and 20: even or not")
for i in range(20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")
        
def is_multiple3(m):
    """
    input: m, a positive integer
    returns True if m is multiple of 3, otherwise false
    """
    
    remainder = m % 3
    return remainder == 0
print ("Is it a multiple of 3?")
for m in range(40):
    if is_multiple3(m):
        print(m, "yes")
    else:
        print(m, "no")