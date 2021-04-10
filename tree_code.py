# -*- coding: utf-8 -*-
"""
Created on Thu May 16 10:37:40 2019

author: Ayush Kumar
coauthor: Tushar Banka
"""

import pandas as pd
import numpy as np

df=pd.read_excel('mesoamerica_lulc EL tuma (Autosaved).xlsx',sheet_name='Sheet2')  #read the file


#to add blank columns
no_of_cols = df.shape[1]

col=list(df.columns)

for word in col:
    col=list(df.columns)
    if word[0]=='b' and len(word)==10:      #will be changed to'b' for other files
        if int(word[-1])>3:
            df.insert(col.index(word)+1,"TrHeight"+word[-3]+'_'+(word[-1]), (" ")*no_of_cols,True)
            df.insert(col.index(word)+1,"TrDBH"+word[-3]+'_'+(word[-1]), (" ")*no_of_cols,True)
    elif word[0]=='b' and len(word)==11:
            df.insert(col.index(word)+1,"TrHeight"+word[-4]+'_'+(word[-2:-1]), (" ")*no_of_cols,True)
            df.insert(col.index(word)+1,"TrDBH"+word[-4]+'_'+(word[-2:-1]), (" ")*no_of_cols,True)
            
#added blank columns
            
#df.to_csv('testing.csv')

#creates a list of subplot and tree         
all_col=list(df.columns)
sub=[]
tree=[]


for word in all_col:
    all_col=list(df.columns)
    if word[0]=='b' and len(word)==10:
        sub.append(int(word[-3]))
        tree.append(int(word[-1]))
    elif word[0]=='b' and len(word)==11 :
        sub.append(int(word[-4]))
        tree.append(int(word[-2:]))
    if(word=='TrSuPlSpecies1_1'):
        divide_index=all_col.index(word)



df.shape
nrows=int((df.shape[1]-divide_index)/4)*(df.shape[0])
ds2=df.iloc[:, divide_index:df.shape[1]]     #this 3 will have to be changed according to the file
ds3=pd.DataFrame(ds2.values.reshape(nrows,4))




df4=df.iloc[:, 0:divide_index]   #this 3 will have to be changed according to the file
df4.shape[1]
m=[]
result=ds3


for i in range(df4.shape[1]):
    m=df4.iloc[:,df4.shape[1]-1-i]
    
    m=pd.DataFrame((np.repeat(m,((df.shape[1]-divide_index)/4)))).reset_index()
    m.drop(['index'],axis=1,inplace=True)
    result=pd.concat([m,result],axis=1,ignore_index=True)

 

sub=sub*(int(result.shape[0]/len(sub)))
tree=tree*(int(result.shape[0]/len(tree)))
result.insert(divide_index,'Subplot',sub,True)
result.insert(divide_index+1,'Tree',tree,True)

result.columns=['Landscape','CID','new_SID','Cluster','Plot','Subplot','Tree','TrSuPlSpecies','Botname','TrHeight','TrDBH']

result.to_csv('mesoamerica_lulc EL tuma (Autosaved)_sheet2.csv')