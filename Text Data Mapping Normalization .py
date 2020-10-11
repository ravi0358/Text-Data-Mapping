#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz


# In[2]:


df = pd.read_csv('Second_Iteration_NEW.csv')


# In[3]:


del df['Unnamed: 0']


# In[4]:


df.shape


# In[5]:


df.fillna('NA',inplace=True)


# In[6]:


ids = {'root':['ST','RD','W','AVE','STR','DR','E','S','N','APT','HWY','PL','PO','TER','SW','NE','SE','NW','MN','STR.'],
       'abb':['STREET','ROAD','WEST','AVENUE','STREET','DRIVE','EAST','SOUTH','NORTH','APARTMENT','HIGHWAY','PLACE',
             'POST OFFICE','TERRACE','SOUTH WEST','NORTH EAST','SOUTH EAST','NORTH WEST','MAIN','STREET']}
       
ids = dict(zip(ids['root'], ids['abb']))


# In[7]:


ids


# In[8]:


def Convert(string): 
    li = list(string.split(" ")) 
    return li 

def Map_Normalize(df,feature):
    Feature_1= df.apply(lambda x:Convert(x[feature]),axis=1)
    a=[]
    for i in Feature_1.tolist():
        k=[]
        for j in i:
            k.append(ids.get(j,j))
        a.append(k)
    Feature_df= pd.DataFrame(a)
    Feature_df['merged'] = Feature_df.stack().astype(str).groupby(level=0).agg(' '.join)
    Feature_df= Feature_df['merged']
    df[feature]=Feature_df
    return df

# def Map_Normalizeing(df,features):
#     for i in features:
#         df =Map_Normalize(df,i)
#     return df


# In[9]:


df.head()


# In[10]:


features = ['address','line_1_address']


# In[11]:


df_1 = Map_Normalize(df,'line_1_address')


# In[12]:


df_1.head()


# In[15]:


df_1['New_Map_Address'] = df_1.apply(lambda x: fuzz.token_sort_ratio(x['address'], x['line_1_address']), axis=1)


# In[16]:


df_1


# In[17]:


df_1.columns


# # Droping Stopwords

# In[19]:


dropWords = ["CORPORATION","LIMITED","CORP","GROUP","PRIVATE","PVT","LTD",".","COMPANY",
             "INC","CO","PTE","TECHNOLOGY","PLC","THE"]


# In[20]:


words = df.company_name.str.split(expand=True).stack()
words = words[words.isin(dropWords)]
words.value_counts()


# In[21]:


pat = r'\b(?:{})\b'.format('|'.join(dropWords))


# In[ ]:


df['company_name'] = df['company_name'].str.replace(pat, ' ')


# In[ ]:


# a=[]
# for i in aaa.tolist():
#     k=[]
#     for j in i:
#         k.append(ids.get(j,j))
#     a.append(k)
# aa=pd.DataFrame(a)


# In[ ]:





# In[ ]:


# a = [1, 2, 3, 4, 1, 5, 3, 2, 6, 1, 1]
# dic = {1:10, 2:20, 3:'foo'}

# print([dic.get(n, n) for n in a])


# In[ ]:





# In[ ]:





# In[ ]:




