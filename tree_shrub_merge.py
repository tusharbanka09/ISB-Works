# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:34:40 2019

@author: Ayush Kumar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# vertical format

fileS = 'Sarolangun_shrub_final'
fileT = 'Sarolangun_tree_final'
#dfs = pd.read_csv(fileS +'.csv', encoding = 'unicode_escape')
#dft = pd.read_csv(fileT +'.csv', encoding = 'unicode_escape')

dfs = pd.read_excel(fileS + '.xlsx',sheet_name='in')
dft = pd.read_excel(fileT + '.xlsx',sheet_name='in')

# handling the tree file
dft.drop(['Unnamed: 0','Tree'], axis = 1, inplace = True)

dft.insert(6,'P-Type', ('T'),True)
dft = dft[['Landscape', 'CID', 'new_SID', 'Cluster', 'Plot', 'Subplot', 'P-Type', 'TrDBH', 'TrHeight', 'TrSuPlSpecies', 'Botname', 'Inconsistency']]
dft.insert(9,'Length', (''),True)
dft.insert(10,'Width', (''),True)
dft.columns =['Landscape', 'CID', 'new_SID', 'Cluster', 'Plot', 'Subplot', 'P-Type','DBH', 'Height', 'Length', 'Width', 'SuPlSpecies', 'Botname','Inconsistency']

# handling the shrubs
dfs.drop(['Unnamed: 0','Shrub'], axis = 1, inplace = True)

dfs.insert(6,'P-Type', ('S'),True)
dfs=dfs[['Landscape','CID','new_SID','Cluster','Plot','Subplot','P-Type','ShHeight','ShLength','ShWidth','ShSuPlSpecies','Botname','Inconsistency']]
dfs.insert(7,'DBH', (''),True)
dfs.columns =['Landscape', 'CID', 'new_SID', 'Cluster', 'Plot', 'Subplot', 'P-Type','DBH', 'Height', 'Length', 'Width', 'SuPlSpecies', 'Botname','Inconsistency']

result = pd.concat([dft,dfs])
result.to_csv(fileS+'_merged.csv')
################################################################################################################

# horizontal format

'''fileS = 'Columbus Mine_shrub_final' # shrub file long format
fileT = 'Columbus Mine_tree_final' # tree file long format
ds = pd.read_csv(fileS +'.csv')
dt = pd.read_csv(fileT +'.csv')

dt.drop(['Unnamed: 0'], axis = 1, inplace = True)
ds.drop(['Unnamed: 0'], axis = 1, inplace = True)

ds.replace(to_replace = '                                                                                     ' , value = np.nan , inplace = True) # replace the value present in empty cells
dt.replace(to_replace = '                                                             ' , value = np.nan , inplace = True) # replace the value present in empty cells

# creates a list of column names with Sh at the beginning of botname
s = []
for i in range(ds.shape[1]):
    if ds.columns[i] == 'Botname':
        s.append('Sh'+ds.columns[i])
    else:
        s.append(ds.columns[i])
ds.columns = s

# creates a list of column names with Tr at the beginning of botname
t = []
for i in range(dt.shape[1]):
    if dt.columns[i] == 'Botname':
        t.append('Tr'+dt.columns[i])
    else:
        t.append(dt.columns[i])
dt.columns = t

result = pd.merge(ds, dt, how='outer', on=['Landscape','CID','new_SID','Cluster','Plot','Subplot','T-S']) # merges the two file using the columns 'Landscape','CID','new_SID','Cluster','Plot','Subplot','T-S' as keys
result.to_csv('tree_shrub_columbus_merged.csv') # putting the data to a new file'''