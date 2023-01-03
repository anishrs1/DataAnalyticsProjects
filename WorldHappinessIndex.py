#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt


# In[2]:


import seaborn as sns


# In[4]:


data_19 = pd.read_csv("C:/Users/anish/OneDrive/Desktop/Data Analytics/Data Analyst Datasets/WorldHappinessReport/2019.csv");


# In[5]:


data_19.info()


# In[7]:


data_19.describe()


# In[8]:


data_19.corr()


# In[9]:


plt.figure(figsize=(16,10))  # on this line I just set the size of figure to 12 by 10.
sns.heatmap(data_19.corr(), annot=True, linewidths=1, cmap="ocean_r", fmt=".2f")  # seaborn has very simple solution for heatmap

plt.suptitle("Correlation Map", fontsize=18)

plt.show()   # whitest and greenest are most correlated


# In[10]:


plt.clf()  # to clear our plots before re-creating them.

plt.figure(figsize=(16,15));  # to make it easy to divide and see

plt.subplot(3,1,1);      # 1st row 
plt.scatter(data_19['Happiness Score'], data_19['Economy (GDP per Capita)'], color='g');
plt.xlabel("Happiness Score");
plt.ylabel("Economy");

plt.subplot(3,1,2);     # 2nd row
plt.scatter(data_19['Happiness Score'], data_19['Family'], color='b');
plt.xlabel("Happiness Score");
plt.ylabel("Family");

plt.subplot(3,1,3);     # 3rd row
plt.scatter(data_19['Happiness Score'], data_19['Health (Life Expectancy)'], color='r');
plt.xlabel("Happiness Score");
plt.ylabel("Health");


plt.suptitle("FAMILY / ECONOMY / HEALTH",fontsize=18)
plt.tight_layout()
plt.show()


# In[11]:


plt.clf()  # to clear our plots before re-creating them.

plt.figure(figsize=(16,15));  # to make it easy to divide and see

plt.subplot(3,1,1);      # 1st row 
plt.scatter(data_19['Score'], data_19['GDP per capita'], color='g');
plt.xlabel("Happiness Score");
plt.ylabel("Economy");

plt.subplot(3,1,2);     # 2nd row
plt.scatter(data_19['Score'], data_19['Social support'], color='b');
plt.xlabel("Happiness Score");
plt.ylabel("Family");

plt.subplot(3,1,3);     # 3rd row
plt.scatter(data_19['Score'], data_19['Healthy life expectancy'], color='r');
plt.xlabel("Happiness Score");
plt.ylabel("Health");


plt.suptitle("FAMILY / ECONOMY / HEALTH",fontsize=18)
plt.tight_layout()
plt.show()


# In[12]:


plt.clf()  # to clear our plots before re-creating them.

plt.figure(figsize=(16,15));  # to make it easy to divide and see

plt.subplot(3,1,1);      # 1st row 
plt.scatter(data_19['Score'], data_19['GDP per capita'], color='g');
plt.xlabel("Happiness Score");
plt.ylabel("Economy");

plt.subplot(3,1,2);     # 2nd row
plt.scatter(data_19['Score'], data_19['Social support'], color='b');
plt.xlabel("Happiness Score");
plt.ylabel("Family");

plt.subplot(3,1,3);     # 3rd row
plt.scatter(data_19['Score'], data_19['Healthy life expectancy'], color='r');
plt.xlabel("Happiness Score");
plt.ylabel("Health");


plt.suptitle("FAMILY / ECONOMY / HEALTH",fontsize=18)
plt.tight_layout()
plt.show()


# In[ ]:




