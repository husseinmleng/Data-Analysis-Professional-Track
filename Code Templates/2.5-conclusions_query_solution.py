#!/usr/bin/env python
# coding: utf-8

# # Drawing Conclusions Using Query

# In[1]:


# Load 'winequality_edited.csv,' a file you created in a previous section 
import pandas as pd

df = pd.read_csv('winequality_edited.csv')
df.head()


# ### Do wines with higher alcoholic content receive better ratings?

# In[2]:


# get the median amount of alcohol content
df.alcohol.median()


# In[4]:


# select samples with alcohol content less than the median
low_alcohol = df.query('alcohol < 10.3')

# select samples with alcohol content greater than or equal to the median
high_alcohol = df.query('alcohol >= 10.3')

# ensure these queries included each sample exactly once
num_samples = df.shape[0]
num_samples == low_alcohol['quality'].count() + high_alcohol['quality'].count() # should be True


# In[5]:


# get mean quality rating for the low alcohol and high alcohol groups
low_alcohol.quality.mean(), high_alcohol.quality.mean()


# ### Do sweeter wines receive better ratings?

# In[6]:


# get the median amount of residual sugar
df.residual_sugar.median()


# In[7]:


# select samples with residual sugar less than the median
low_sugar = df.query('residual_sugar < 3')

# select samples with residual sugar greater than or equal to the median
high_sugar = df.query('residual_sugar >= 3')

# ensure these queries included each sample exactly once
num_samples == low_sugar['quality'].count() + high_sugar['quality'].count() # should be True


# In[8]:


# get mean quality rating for the low sugar and high sugar groups
low_sugar.quality.mean(), high_sugar.quality.mean()


# In[ ]:




