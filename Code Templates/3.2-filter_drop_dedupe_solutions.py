#!/usr/bin/env python
# coding: utf-8

# # Filter, Drop Nulls, Dedupe
# Use `data_08_v1.csv` and `data_18_v1.csv`

# In[1]:


# load datasets
import pandas as pd

df_08 = pd.read_csv('data_08_v1.csv')
df_18 = pd.read_csv('data_18_v1.csv')


# In[2]:


# view dimensions of dataset
df_08.shape


# In[3]:


# view dimensions of dataset
df_18.shape


# ## Filter by Certification Region

# In[4]:


# filter datasets for rows following California standards
df_08 = df_08.query('cert_region == "CA"')
df_18 = df_18.query('cert_region == "CA"')


# In[5]:


# confirm only certification region is California
df_08['cert_region'].unique()


# In[6]:


# confirm only certification region is California
df_18['cert_region'].unique()


# In[7]:


# drop certification region columns form both datasets
df_08.drop('cert_region', axis=1, inplace=True)
df_18.drop('cert_region', axis=1, inplace=True)


# In[8]:


df_08.shape


# In[9]:


df_18.shape


# ## Drop Rows with Missing Values

# In[10]:


# view missing value count for each feature in 2008
df_08.isnull().sum()


# In[11]:


# view missing value count for each feature in 2018
df_18.isnull().sum()


# In[12]:


# drop rows with any null values in both datasets
df_08.dropna(inplace=True)
df_18.dropna(inplace=True)


# In[13]:


# checks if any of columns in 2008 have null values - should print False
df_08.isnull().sum().any()


# In[14]:


# checks if any of columns in 2018 have null values - should print False
df_18.isnull().sum().any()


# ## Dedupe Data

# In[15]:


# print number of duplicates in 2008 and 2018 datasets
print(df_08.duplicated().sum())
print(df_18.duplicated().sum())


# In[16]:


# drop duplicates in both datasets
df_08.drop_duplicates(inplace=True)
df_18.drop_duplicates(inplace=True)


# In[17]:


# print number of duplicates again to confirm dedupe - should both be 0
print(df_08.duplicated().sum())
print(df_18.duplicated().sum())


# In[18]:


# save progress for the next section
df_08.to_csv('data_08_v2.csv', index=False)
df_18.to_csv('data_18_v2.csv', index=False)


# In[ ]:




