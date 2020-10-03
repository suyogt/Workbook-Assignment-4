#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


Location = "C:/Users/Suyog Thengale/Desktop/datasets/gradedata.csv"


# In[4]:


df = pd.read_csv(Location)


# In[5]:


df.head()


# In[6]:


import numpy as np


# In[7]:


df['timemgmt'] = np.where((df['exercise']>3) & (df['hours']>17),'yes','no')


# In[8]:


df


# In[ ]:




