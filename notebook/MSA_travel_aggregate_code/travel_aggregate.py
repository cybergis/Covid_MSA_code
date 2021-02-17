#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd


# In[38]:


def aggregate_MSA(input_data, write_path):
    
    city_state = pd.read_csv('us city by state.csv')
    metro_county = pd.read_csv('metro_county.csv')
    travel_count = pd.read_csv(input_data)
    
    
    
    travel_count['state'] = 's'

    for i in range(len(travel_count)):
        if (len(travel_count.at[i,'city'].split(', ')) > 1):
            travel_count.at[i, 'state'] = travel_count.at[i, 'city'].split(', ')[1]
            travel_count.at[i, 'city'] = travel_count.at[i, 'city'].split(', ')[0]
    
       
    merged1 = travel_count.merge(city_state, how = 'inner', 
                            left_on=['city', 'state'], 
                            right_on=['City','State short'])
        
        

    
    for i in range(len(merged1)):
        merged1.at[i, 'County'] = merged1.at[i, 'County'].lower()
    
    
    for i in range(len(metro_county)):
        metro_county.at[i, 'name10_county'] = metro_county.at[i, 'name10_county'].lower()
 
    merged1 = merged1.drop_duplicates(subset = ['city', 'state'])
    
    
    merged2 = merged1.merge(metro_county, how = 'inner',
                        left_on=['County', 'state'], 
                        right_on=['name10_county','states_msa'])
    
    
    merged2 = merged2.drop(columns=['City', 'city', 'geoid_msa', 'State full', 'statefp10_county', 'countyfp10'
                         , 'countyns10', 'geoid10_county', 'name10_county', 'countyid', 'states_msa_full'
                         , 'states_msa', 'states_msa_code', 'City alias', 'state', 'State short', 'County'])
    merged2 = merged2.groupby(['name_msa']).sum()
    merged2.to_csv(write_path)
    
    
    
    
    
    
    


# In[39]:


if __name__ == "__main__":
    aggregate_MSA('traveler to each city.csv','output.csv')

