#!/usr/bin/env python
# coding: utf-8

# In[1]:


# imports and load data
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('store_data.csv')
df.head()


# In[2]:


# explore data
df.tail(20)


# In[3]:


# sales for the last month
df.iloc[196:, 1:].sum().plot(kind='bar');


# In[4]:


# average sales
df.mean().plot(kind='pie');


# In[5]:


# sales for the week of March 13th, 2016
sales = df[df['week'] == '2016-03-13']
sales.iloc[0, 1:].plot(kind='bar');


# In[6]:


# sales for the lastest 3-month periods
last_three_months = df[df['week'] >= '2017-12-01']
last_three_months.iloc[:, 1:].sum().plot(kind='pie')


# In[ ]:




