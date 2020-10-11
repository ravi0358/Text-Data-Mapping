#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz


# In[2]:


df1 = pd.read_csv('HG Data.csv')
df2 = pd.read_csv('CRT_DNB.csv')


# In[3]:


df1.head()


# In[4]:


df1.columns


# In[5]:


df1['RowNum'] = np.arange(len(df1))


# In[6]:


df1


# In[7]:


df2


# In[8]:


def Mapping(x1,x2,x3,x4,x5,x6,x7,x8,x9):
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    g=[]
    h=[]
    k=[]
    l=[]
    m=[]
    n=[]
    row=[]
    for i in x1:
        for j in x2:
            a.append(i)
            b.append(j)
            c.append(fuzz.token_sort_ratio(i,j))
    for i in x3:
        for j in x4:
            d.append(i)
            e.append(j)
            f.append(fuzz.token_sort_ratio(i,j))
    for i in x5:
        for j in x6:
            g.append(i)
            h.append(j)
            k.append(fuzz.token_sort_ratio(i,j))
    for i in x7:
        for j in x8:
            l.append(i)
            m.append(j)
            n.append(fuzz.token_sort_ratio(i,j))
        for i in x9:
            row.append(i)
    return a,b,c,d,e,f,g,h,k,l,m,n,row

def New_df(x1,x2,x3,x4,x5,x6,x7,x8,x9):
    Records = Mapping(x1,x2,x3,x4,x5,x6,x7,x8,x9)
    Records= np.array(Records).transpose().tolist()
    df_1 = pd.DataFrame(Records)
    df_1.columns = ['Company1','Comapny2','Company_Map','Satte1','State2','State_Map','City1','City2','City_Map',
                   'Addre1','Addre2','Add_Map','Row']
    return df_1


# In[9]:


New_df(df1['COMPANY'],df2['PARTY_NAME'],df1['STATE'],df2['PARTY_STATE'],df1['CITY'],df2['PARTY_CITY'],df1['ADDRESS'],df2['PARTY_ADDRESS1'],df1['RowNum'])


# In[ ]:




