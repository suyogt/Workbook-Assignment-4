#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[5]:


Location = "C:/Users/Suyog Thengale/Desktop/datasets/gradedata.csv"


# In[6]:


df = pd.read_csv(Location)


# In[7]:


df.head()


# In[8]:


bins = [0, 80, 100]


# In[11]:


group_names = ['Fail', 'Pass']


# In[12]:


df['Pass or Fail'] = pd.cut(df['grade'], bins, labels=group_names)


# In[13]:


df


# In[ ]:




