#!/usr/bin/env python
# coding: utf-8

# # Plotting with Matplotlib
# Use Matplotlib to create bar charts that visualize the conclusions you made with groupby and query.

# In[1]:


# Import necessary packages and load `winequality_edited.csv`
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('winequality_edited.csv')
df.head()


# ### #1: Do wines with higher alcoholic content receive better ratings?
# Create a bar chart with one bar for low alcohol and one bar for high alcohol wine samples. This first one is filled out for you.

# In[2]:


# Use query to select each group and get its mean quality
median = df['alcohol'].median()
low = df.query('alcohol < {}'.format(median))
high = df.query('alcohol >= {}'.format(median))

mean_quality_low = low['quality'].mean()
mean_quality_high = high['quality'].mean()


# In[3]:


# Create a bar chart with proper labels
locations = [1, 2]
heights = [mean_quality_low, mean_quality_high]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Alcohol Content')
plt.xlabel('Alcohol Content')
plt.ylabel('Average Quality Rating');


# ### #2: Do sweeter wines receive higher ratings?
# Create a bar chart with one bar for low residual sugar and one bar for high residual sugar wine samples.

# In[4]:


# Use query to select each group and get its mean quality
median = df['residual_sugar'].median()
low = df.query('residual_sugar < {}'.format(median))
high = df.query('residual_sugar >= {}'.format(median))

mean_quality_low = low['quality'].mean()
mean_quality_high = high['quality'].mean()


# In[5]:


# Create a bar chart with proper labels
locations = [1, 2]
heights = [mean_quality_low, mean_quality_high]
labels = ['Low', 'High']
plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Residual Sugar')
plt.xlabel('Residual Sugar')
plt.ylabel('Average Quality Rating');


# ### #3: What level of acidity receives the highest average rating?
# Create a bar chart with a bar for each of the four acidity levels.

# In[6]:


# Use groupby to get the mean quality for each acidity level
acidity_level_quality_means = df.groupby('acidity_levels').quality.mean()
acidity_level_quality_means


# In[7]:


# Create a bar chart with proper labels
locations = [4, 1, 2, 3]  # reorder values above to go from low to high
heights = acidity_level_quality_means

# labels = ['Low', 'Medium', 'Moderately High', 'High']
labels = acidity_level_quality_means.index.str.replace('_', ' ').str.title() # alternative to commented out line above

plt.bar(locations, heights, tick_label=labels)
plt.title('Average Quality Ratings by Acidity Level')
plt.xlabel('Acidity Level')
plt.ylabel('Average Quality Rating');


# In[ ]:




