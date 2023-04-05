#!/usr/bin/env python
# coding: utf-8

# # EDA with Visuals
# Create visualizations to answer the quiz questions below this notebook. Use `winequality_edited.csv`. You should've created this data file in the previous section: *Appending Data (cont.)*.

# In[1]:


# Load dataset
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('winequality_edited.csv')


# In[2]:


df.head()


# ### Histograms for Various Features

# In[3]:


df.fixed_acidity.hist();


# In[4]:


df.total_sulfur_dioxide.hist();


# In[5]:


df.pH.hist();


# In[6]:


df.alcohol.hist();


# ### Scatterplots of Quality Against Various Features

# In[7]:


df.plot(x="volatile_acidity", y="quality", kind="scatter");


# In[8]:


df.plot(x="residual_sugar", y="quality", kind="scatter");


# In[9]:


df.plot(x="pH", y="quality", kind="scatter");


# In[10]:


df.plot(x="alcohol", y="quality", kind="scatter");


# In[ ]:




