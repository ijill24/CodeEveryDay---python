# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:52:55 2020

@author: Jillian
"""
#MIT 60001 Introduction to Computer Science and Programming in Python
#Dr. Ana Bell Problem Set 1

#In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery).  Modify
#your program to include the following
#1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
#2. After the 6th month, increase your salary by that percentage.  Do the same after the 12
#th
#th
#month, the 18  month, and so on. 
#Write a program to calculate how many months it will take you save up enough money for a down
#payment.  LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the
#required down payment percentage is 0.25 (or 25%).  Have the user enter the following variables:
#1. The starting annual salary (annual_salary)
#2
#2. The percentage of salary to be saved (portion_saved)
#3. The cost of your dream home (total_cost)
#4. The semi­annual salary raise (semi_annual_raise)

annual_salary = float(input("What is your starting annual salary?"))
portion_saved = float(input("What portion of your salary will be saved, as a decimal?"))
total_cost = float(input("What is the total cost of your dream home?"))
annual_raise = float(input("Enter your semi-annual raise, as a decimal:"))

portion_down_payment = 0.25 * total_cost
monthly_salary = annual_salary / 12
current_savings = 0.00
r = 0.04
month = 0

def updated_salary(annual_salary, annual_raise):
    """
    input: uses annual salary and annual raise to compute new yearly salary after raise
    returns: new salary after getting a raise
    """
    updated_salary = annual_salary + (annual_salary * annual_raise)
    return updated_salary;

while current_savings < portion_down_payment:
    month += 1
    if month % 6 == 0:
        annual_salary = updated_salary(annual_salary, annual_raise)
        monthly_salary = annual_salary / 12
        monthly_saving = (portion_saved * monthly_salary)
        investments = (current_savings * r / 12)
        current_savings += investments + monthly_saving
    else:
        monthly_saving = (portion_saved * monthly_salary)
        investments = (current_savings * r / 12)
        current_savings += investments + monthly_saving
print("Number of months:", month)
 