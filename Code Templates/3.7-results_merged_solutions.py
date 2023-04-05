#!/usr/bin/env python
# coding: utf-8

# # Results with Merged Dataset
# #### Q5: For all of the models that were produced in 2008 that are still being produced now, how much has the mpg improved and which vehicle improved the most?
# Remember to use your new dataset, `combined_dataset.csv`

# In[1]:


# load dataset
import pandas as pd
df = pd.read_csv('combined_dataset.csv')


# ### 1. Create a new dataframe, `model_mpg`, that contain the mean combined mpg values in 2008 and 2018 for each unique model
# 
# To do this, group by `model` and find the mean `cmb_mpg_2008` and mean `cmb_mpg` for each.

# In[2]:


model_mpg = df.groupby('model').mean()[['cmb_mpg_2008', 'cmb_mpg']]


# In[3]:


model_mpg.head()


# ### 2. Create a new column, `mpg_change`, with the change in mpg
# Subtract the mean mpg in 2008 from that in 2018 to get the change in mpg

# In[4]:


model_mpg['mpg_change'] = model_mpg['cmb_mpg'] - model_mpg['cmb_mpg_2008']


# In[5]:


model_mpg.head()


# ### 3. Find the vehicle that improved the most
# Find the max mpg change, and then use query or indexing to see what model it is!

# In[6]:


max_change = model_mpg['mpg_change'].max()
max_change


# In[7]:


model_mpg[model_mpg['mpg_change'] == max_change]


# Pandas also has a useful [`idxmax`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.idxmax.html) function you can use to find the index of the row containing a column's maximum value!

# In[8]:


idx = model_mpg.mpg_change.idxmax()
idx


# In[9]:


model_mpg.loc[idx]


# In[ ]:




