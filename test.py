#!/usr/bin/env python
# coding: utf-8

# In[8]:


import matplotlib.pyplot as plt
import pandas as pd


# In[9]:


df = pd.read_csv("output.csv")
df = df.loc[df['name_msa'] == 'Los Angeles-Long Beach-Anaheim']


# In[10]:


df.plot(x = 'group', y = 'cases')
plt.xlabel('date',fontsize=18)
plt.ylabel('Cases',fontsize=18)
plt.show()

