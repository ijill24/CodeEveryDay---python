# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 18:19:42 2020

@author: Jillian
"""

#import pandas as pd
#filename = 'philly.csv'
#data=pd.read_csv(filename)
#print(data.head())

import pandas as pd
filename = 'philly.csv'
data = pd.read_csv(filename)
data_array = data.values
print(data)