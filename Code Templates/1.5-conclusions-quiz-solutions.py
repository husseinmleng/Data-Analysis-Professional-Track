#!/usr/bin/env python
# coding: utf-8

# # Drawing Conclusions Quiz
# Use the space below to explore `store_data.csv` to answer the quiz questions below.

# In[1]:


# imports and load data
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('store_data.csv')
df.head()


# In[2]:


# explore data
df.hist(figsize=(8, 8));


# In[3]:


df.tail(20)


# In[4]:


# total sales for the last month
df.iloc[196:, 1:].sum()


# In[5]:


# average sales
df.mean()


# In[6]:


# sales on march 13, 2016
df[df['week'] == '2016-03-13']


# In[7]:


# worst week for store C
df[df['storeC'] == df['storeC'].min()]


# In[8]:


# total sales during most recent 3 month period
last_three_months = df[df['week'] >= '2017-12-01']
last_three_months.iloc[:, 1:].sum()  # exclude sum of week column


# In[ ]:




