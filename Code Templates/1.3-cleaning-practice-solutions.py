#!/usr/bin/env python
# coding: utf-8

# # Cleaning Practice
# Let's first practice handling missing values and duplicate data with `cancer_data_means.csv`.

# In[1]:


# import pandas and load cancer data
import pandas as pd

df = pd.read_csv('cancer_data_means.csv')

# check which columns have missing values with info()
df.info()


# In[2]:


# use means to fill in missing values
df.fillna(df.mean(), inplace=True)

# confirm your correction with info()
df.info()


# In[3]:


# check for duplicates in the data
sum(df.duplicated())


# In[4]:


# drop duplicates
df.drop_duplicates(inplace=True)


# In[5]:


# confirm correction by rechecking for duplicates in the data
sum(df.duplicated())


# ## Renaming Columns
# Since we also previously changed our dataset to only include means of tumor features, the "_mean" at the end of each feature seems unnecessary. It just takes extra time to type in our analysis later. Let's come up with a list of new labels to assign to our columns.

# In[6]:


# remove "_mean" from column names
new_labels = []
for col in df.columns:
    if '_mean' in col:
        new_labels.append(col[:-5])  # exclude last 6 characters
    else:
        new_labels.append(col)

# new labels for our columns
new_labels


# In[7]:


# assign new labels to columns in dataframe
df.columns = new_labels

# display first few rows of dataframe to confirm changes
df.head()


# In[8]:


# save this for later
df.to_csv('cancer_data_edited.csv', index=False)


# In[ ]:




