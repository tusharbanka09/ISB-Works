# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:37:40 2019

author: Ayush Kumar
"""

import pandas as pd
import numpy as np

file = 'sample' # write the file name within quotes

#df = pd.read_excel(file+'.xlsx',sheet_name='Sheet1')  # read the file. Write the sheet name of your excel sheet in the sheet_name argument
#df = pd.read_csv(file+'.csv')

# code segment to add blank columns after Botname column from the fourth tree onwards
no_of_cols = df.shape[1]
col=list(df.columns)
for word in col:
    col=list(df.columns)
    if word[0]=='B' and len(word)==10:      #looks for the Botname column in the wide file
        if int(word[-1])>3:
            df.insert(col.index(word)+1,"ShHeight"+word[-3]+'_'+(word[-1]), (" ")*no_of_cols,True)
            df.insert(col.index(word)+1,"ShLength"+word[-3]+'_'+(word[-1]), (" ")*no_of_cols,True)
            df.insert(col.index(word)+1,"ShWidth"+word[-3]+'_'+(word[-1]), (" ")*no_of_cols,True)
    elif word[0]=='B' and len(word)==11:
            df.insert(col.index(word)+1,"ShHeight"+word[-4]+'_'+(word[-2:-1]), (" ")*no_of_cols,True)
            df.insert(col.index(word)+1,"ShLength"+word[-4]+'_'+(word[-2:-1]), (" ")*no_of_cols,True)
            df.insert(col.index(word)+1,"ShWidth"+word[-4]+'_'+(word[-2:-1]), (" ")*no_of_cols,True)
#added blank columns

#creates a list of subplot and tree         
all_col=list(df.columns)
sub=[]
tree=[]
for word in all_col:
    all_col=list(df.columns)
    if(word=='ShSuPlSpecies1_1'):
        divide_index=all_col.index(word) # demarkates the column from where columns to be repeated end and columns containing data to be reshaped appear
    if word[0]=='B' and len(word)==10:
        sub.append(int(word[-3]))
        tree.append(int(word[-1]))
    elif word[0]=='B' and len(word)==11 :
        sub.append(int(word[-4]))
        tree.append(int(word[-2:-1]))

nrows=int((df.shape[1]-divide_index)/5)*(df.shape[0]) # 5 as each shrub has species name, botname, height, length, width
ds2=df.iloc[:, divide_index:df.shape[1]]
ds3=pd.DataFrame(ds2.values.reshape(nrows,5)) # reshapes the data such that variables for each successive tree appears underneath the other

df4=df.iloc[:, 0:divide_index]
m=[]
result=ds3
for i in range(df4.shape[1]):
    m=df4.iloc[:,df4.shape[1]-1-i]
    m=pd.DataFrame((np.repeat(m,((df.shape[1]-divide_index)/5)))).reset_index() # duplicates the identifying features (cluster, plot etc.) for each shrub
    m.drop(['index'],axis=1,inplace=True)
    result=pd.concat([m,result],axis=1,ignore_index=True)

sub=sub*(int(result.shape[0]/len(sub)))
tree=tree*(int(result.shape[0]/len(tree)))
result.insert(divide_index,'Subplot',sub,True) # Adds the subplot column
result.insert(divide_index+1,'Shrub',tree,True) # Adds the shrub column

result.columns=['Landscape','CID','new_SID','Cluster','Plot','Subplot','Shrub','ShSuPlSpecies','Botname','ShHeight','ShLength','ShWidth'] # column names
result.to_csv(file+'_final.csv') # putting the data to a file with _final at the end of the original name