#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("Covid-19 data (unsorted).csv")
copy = pd.read_csv("Covid-19 data (unsorted).csv")
data = data.sort_values(by=['county', 'state'])
copy = copy.sort_values(by=['county', 'state'])
print(len(data.index))
data.to_csv("daily count.csv", index = False)
data = pd.read_csv("daily count.csv")
copy.to_csv("daily count_copy.csv", index = False)
copy = pd.read_csv("daily count_copy.csv")
copy
#data.at[5000, 'county']


# In[3]:


i = 1
data['fips'] = data['fips'].fillna(-1)
while i < len(data.index):
    if data.at[i, 'county'] == data.at[i - 1, 'county'] and data.at[i, 'state'] == data.at[i - 1, 'state']:
        if (data.at[i, 'cases'] < copy.at[i - 1, 'cases']):
            data.at[i, 'cases'] = copy.at[i - 1, 'cases']
        if (data.at[i, 'deaths'] < copy.at[i - 1, 'deaths']):
            data.at[i, 'deaths'] = copy.at[i - 1, 'deaths']
        data.at[i, 'cases'] = data.at[i, 'cases'] - copy.at[i - 1, 'cases']
        data.at[i, 'deaths'] = data.at[i, 'deaths'] - copy.at[i - 1, 'deaths']
    i += 1


# In[4]:


data = data.astype({'fips': int})
data["date"] = pd.to_datetime(data["date"])
data = data.sort_values(by = ['date'])
data.to_csv("daily count.csv", index = False)


# In[ ]:




