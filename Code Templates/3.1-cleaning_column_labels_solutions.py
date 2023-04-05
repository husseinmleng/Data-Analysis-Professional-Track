#!/usr/bin/env python
# coding: utf-8

# # Cleaning Column Labels
# Use `all_alpha_08.csv` and `all_alpha_18.csv`

# In[1]:


# load datasets
import pandas as pd

df_08 = pd.read_csv('all_alpha_08.csv') 
df_18 = pd.read_csv('all_alpha_18.csv')


# In[2]:


# view 2008 dataset
df_08.head(1)


# In[3]:


# view 2018 dataset
df_18.head(1)


# ### Drop Extraneous Columns

# In[4]:


# drop columns from 2008 dataset
df_08.drop(['Stnd', 'Underhood ID', 'FE Calc Appr', 'Unadj Cmb MPG'], axis=1, inplace=True)

# confirm changes
df_08.head(1)


# In[5]:


# drop columns from 2018 dataset
df_18.drop(['Stnd', 'Stnd Description', 'Underhood ID', 'Comb CO2'], axis=1, inplace=True)

# confirm changes
df_18.head(1)


# ### Rename Columns

# In[6]:


# rename Sales Area to Cert Region
df_08.rename(columns={'Sales Area': 'Cert Region'}, inplace=True)

# confirm changes
df_08.head(1)


# In[7]:


# replace spaces with underscores and lowercase labels for 2008 dataset
df_08.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# confirm changes
df_08.head(1)


# In[8]:


# replace spaces with underscores and lowercase labels for 2018 dataset
df_18.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

# confirm changes
df_18.head(1)


# In[9]:


# confirm column labels for 2008 and 2018 datasets are identical
df_08.columns == df_18.columns


# In[10]:


# make sure they're all identical like this
(df_08.columns == df_18.columns).all()


# In[11]:


# save new datasets for next section
df_08.to_csv('data_08_v1.csv', index=False)
df_18.to_csv('data_18_v1.csv', index=False)


# In[ ]:




