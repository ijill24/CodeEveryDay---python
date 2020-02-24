# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 21:39:26 2020

@author: Jillian
"""
#practice: CodingBat function exercises


def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
    return True
  else:
    return False

def sum_double(a, b):
  sum = a + b
  if a == b:
    return (sum * 2)
  else:
    return sum

def diff21(n):
  if n > 21:
    return abs(n - 21) * 2
  else:
      return abs(n - 21) 
