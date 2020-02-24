# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:32:22 2020

@author: Jillian
"""

#fstrings practice

firstname = input("What is your first name?")
lastname = input("What is your last name?")
fullname = f"{firstname} {lastname}"
print(fullname)

message = f"Hello, J{firstname} {lastname}!"
print(message)