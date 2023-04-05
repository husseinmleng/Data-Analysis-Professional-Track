#!/usr/bin/env python
# coding: utf-8

# # Drawing Conclusions
# Use the space below to address questions on datasets `clean_08.csv` and `clean_18.csv`

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# load datasets
df_08 = pd.read_csv('clean_08.csv')
df_18 = pd.read_csv('clean_18.csv')


# In[3]:


df_08.head(1)


# ### Q1: Are more unique models using alternative sources of fuel? By how much?

# Let's first look at what the sources of fuel are and which ones are alternative sources.

# In[4]:


df_08.fuel.value_counts()


# In[5]:


df_18.fuel.value_counts()


# Looks like the alternative sources of fuel available in 2008 are CNG and ethanol, and those in 2018 ethanol and electricity. (You can use Google if you weren't sure which ones are alternative sources of fuel!)

# In[6]:


# how many unique models used alternative sources of fuel in 2008
alt_08 = df_08.query('fuel in ["CNG", "ethanol"]').model.nunique()
alt_08


# In[7]:


# how many unique models used alternative sources of fuel in 2018
alt_18 = df_18.query('fuel in ["Ethanol", "Electricity"]').model.nunique()
alt_18


# In[8]:


plt.bar(["2008", "2018"], [alt_08, alt_18])
plt.title("Number of Unique Models Using Alternative Fuels")
plt.xlabel("Year")
plt.ylabel("Number of Unique Models");


# Since 2008, the number of unique models using alternative sources of fuel increased by 24. We can also look at proportions.

# In[9]:


# total unique models each year
total_08 = df_08.model.nunique()
total_18 = df_18.model.nunique()
total_08, total_18


# In[10]:


prop_08 = alt_08/total_08
prop_18 = alt_18/total_18
prop_08, prop_18


# In[11]:


plt.bar(["2008", "2018"], [prop_08, prop_18])
plt.title("Proportion of Unique Models Using Alternative Fuels")
plt.xlabel("Year")
plt.ylabel("Proportion of Unique Models");


# ### Q2: How much have vehicle classes improved in fuel economy?  

# Let's look at the average fuel economy for each vehicle class for both years.

# In[12]:


veh_08 = df_08.groupby('veh_class').cmb_mpg.mean()
veh_08


# In[13]:


veh_18 = df_18.groupby('veh_class').cmb_mpg.mean()
veh_18


# In[14]:


# how much they've increased by for each vehicle class
inc = veh_18 - veh_08
inc


# In[15]:


# only plot the classes that exist in both years
inc.dropna(inplace=True)
plt.subplots(figsize=(8, 5))
plt.bar(inc.index, inc)
plt.title('Improvements in Fuel Economy from 2008 to 2018 by Vehicle Class')
plt.xlabel('Vehicle Class')
plt.ylabel('Increase in Average Combined MPG');


# ### Q3: What are the characteristics of SmartWay vehicles? Have they changed over time?

# We can analyze this by filtering each dataframe by SmartWay classification and exploring these datasets.

# In[16]:


# smartway labels for 2008
df_08.smartway.unique()


# In[17]:


# get all smartway vehicles in 2008
smart_08 = df_08.query('smartway == "yes"')


# In[18]:


# explore smartway vehicles in 2008
smart_08.describe()


# Use what you've learned so for to further explore this dataset on 2008 smartway vehicles.

# In[19]:


# smartway labels for 2018
df_18.smartway.unique()


# In[20]:


# get all smartway vehicles in 2018
smart_18 = df_18.query('smartway in ["Yes", "Elite"]')


# In[21]:


smart_18.describe()


# Use what you've learned so for to further explore this dataset on 2018 smartway vehicles.

# ### Q4: What features are associated with better fuel economy?

# You can explore trends between cmb_mpg and the other features in this dataset, or filter this dataset like in the previous question and explore the properties of that dataset. For example, you can select all vehicles that have the top 50% fuel economy ratings like this.

# In[22]:


top_08 = df_08.query('cmb_mpg > cmb_mpg.mean()')
top_08.describe()


# In[23]:


top_18 = df_18.query('cmb_mpg > cmb_mpg.mean()')
top_18.describe()


# In[ ]:




