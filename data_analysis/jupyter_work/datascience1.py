#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.listdir()


# In[15]:


import pandas


# In[6]:


df1 = pandas.read_csv("supermarkets.csv")
df1.set_index("ID")


# In[8]:


df1.shape


# In[12]:


df2=pandas.read_json("supermarkets.json")
df2.set_index("ID")


# In[18]:


df3 = pandas.read_excel("supermarkets.xlsx")
df3


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




