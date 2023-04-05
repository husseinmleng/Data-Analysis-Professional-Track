#!/usr/bin/env python
# coding: utf-8

# # Assessing
# Use the space below to explore `winequality-red.csv` and `winequality-white.csv` to answer the quiz questions below.

# In[1]:


import pandas as pd

red_df = pd.read_csv('winequality-red.csv', sep=';')
white_df = pd.read_csv('winequality-white.csv', sep=';')


# In[2]:


print(red_df.shape)
red_df.head()


# In[3]:


print(white_df.shape)
white_df.head()


# In[4]:


red_df.isnull().sum()


# In[5]:


white_df.isnull().sum()


# In[6]:


white_df.duplicated().sum()


# In[7]:


red_df.quality.nunique()


# In[8]:


white_df.quality.nunique()


# In[9]:


red_df.density.mean()


# In[ ]:




