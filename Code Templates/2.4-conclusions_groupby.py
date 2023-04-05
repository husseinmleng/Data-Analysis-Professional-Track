#!/usr/bin/env python
# coding: utf-8

# # Drawing Conclusions Using Groupby

# In[1]:


# Load `winequality_edited.csv`
import pandas as pd

df = pd.read_csv('winequality_edited.csv')


# ### Is a certain type of wine associated with higher quality?

# In[2]:


# Find the mean quality of each wine type (red and white) with groupby
df.groupby('color').mean().quality


# ### What level of acidity receives the highest average rating?

# In[3]:


# View the min, 25%, 50%, 75%, max pH values with Pandas describe
df.describe().pH


# In[4]:


# Bin edges that will be used to "cut" the data into groups
bin_edges = [2.72, 3.11, 3.21, 3.32, 4.01] # Fill in this list with five values you just found


# In[5]:


# Labels for the four acidity level groups
bin_names = ['high', 'mod_high', 'medium', 'low'] # Name each acidity level category


# In[6]:


# Creates acidity_levels column
df['acidity_levels'] = pd.cut(df['pH'], bin_edges, labels=bin_names)

# Checks for successful creation of this column
df.head()


# In[7]:


# Find the mean quality of each acidity level with groupby
df.groupby('acidity_levels').mean().quality


# In[8]:


# Save changes for the next section
df.to_csv('winequality_edited.csv', index=False)

