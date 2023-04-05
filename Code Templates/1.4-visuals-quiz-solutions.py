#!/usr/bin/env python
# coding: utf-8

# # Exploring Data with Visuals Quiz
# Use the space below to explore `powerplant_data_edited.csv` to answer the quiz questions below.

# In[1]:


# imports and load data
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('powerplant_data_edited.csv')
df.head()


# In[2]:


# plot relationship between temperature and electrical output
df.plot(x='temperature', y='energy_output', kind='scatter');


# In[3]:


# plot distribution of humidity
df['humidity'].hist();


# In[4]:


# plot box plots for each variable
df['temperature'].plot(kind='box');


# In[5]:


df['exhaust_vacuum'].plot(kind='box');


# In[6]:


df['pressure'].plot(kind='box');


# In[7]:


df['humidity'].plot(kind='box');


# In[8]:


df['energy_output'].plot(kind='box');


# In[ ]:




