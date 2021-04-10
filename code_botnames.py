# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:44:41 2019

@author: Ayush Kumar
"""
# when working on a tree file in the line 15 and line 26 change 'ShSuPlSpecies' to 'TrSuPlSpecies', when working on a shrub file the code remains as it is

import pandas as pd
import numpy as np

file = 'Ayos_shrub_final'
df=pd.read_csv(file + '.csv', encoding = 'unicode_escape')  #read the file
#df=pd.read_excel(file + '.xlsx', sheet_name='Sheet1')

m = (df['ShSuPlSpecies'].fillna('0')) # remove all the nan values used to check intially can be changed from "0" to "" and then remove the second last line
n = (df['Botname'].fillna('0')) # remove all the nan values

a = m.apply(lambda x: x.strip()) # remove all whitespace from the start and the end of each species name 
b = n.apply(lambda x: x.strip()) # remove all whitespace from the start and the end of each botname

p = pd.Series((pd.Series(a + '@#@' + b)).unique()) # unique values of each pair of species name and botname

dm = pd.DataFrame()
land = 5 # enter the landscape code here

dm['ShSuPlSpecies'] = p.apply(lambda x: x.split('@#@')[0])
dm['Botname'] = p.apply(lambda x: x.split('@#@')[1])
dm.insert(0,'Landscape', land,True)
  
dm['Botname'].replace(to_replace = '0' , value = "" , inplace = True)
dm.to_csv('botnames_'+file + '.csv') # putting the data to a file with botnames_ at the beginning