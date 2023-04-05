#!/usr/bin/env python
# coding: utf-8

# # Merging Datasets
# Use Pandas Merges to create a combined dataset from `clean_08.csv` and `clean_18.csv`.

# In[1]:


# load datasets
import pandas as pd

df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')


# ### Create combined dataset

# In[2]:


# rename 2008 columns
df_08.rename(columns=lambda x: x[:10] + "_2008", inplace=True)


# In[3]:


# view to check names
df_08.head()


# In[4]:


# merge datasets
df_combined = df_08.merge(df_18, left_on='model_2008', right_on='model', how='inner')


# In[5]:


# view to check merge
df_combined.head()


# Save the combined dataset

# In[6]:


df_combined.to_csv('combined_dataset.csv', index=False)

