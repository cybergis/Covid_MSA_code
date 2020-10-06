#!/usr/bin/env python
# coding: utf-8

# In[33]:


import sys
import argparse
import os
import pandas as pd
import datetime as dt
from datetime import timedelta


# In[34]:


def cumulativeToDaily(inputFile):
    data = pd.read_csv(inputFile)
    copy = pd.read_csv(inputFile)
    data = data.sort_values(by=['county', 'state'])
    copy = copy.sort_values(by=['county', 'state'])
    data.to_csv("daily count.csv", index = False)
    data = pd.read_csv("daily count.csv")
    copy.to_csv("daily count_copy.csv", index = False)
    copy = pd.read_csv("daily count_copy.csv")
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
    data = data.astype({'fips': int})
    data["date"] = pd.to_datetime(data["date"])
    data = data.sort_values(by = ['date'])
    # data.to_csv("daily count.csv", index = False)

    return data


# In[35]:


def aggregate(covid, metro, startdate, enddate, interval):
    metro_initial = pd.read_csv(metro)
    metro = pd.read_csv(metro)
    # covid = pd.read_csv(covid)
    i = 0
    while (i < len(metro.index)):
        # print(metro.at[i, 'states_msa'])
        if (metro.at[i, 'states_msa'] == "AL"):
            metro.at[i, 'states_msa'] = "Alabama"
        elif (metro.at[i, 'states_msa'] == "AK"):
            metro.at[i, 'states_msa'] = "Alaska"
        elif (metro.at[i, 'states_msa'] == "AZ"):
            metro.at[i, 'states_msa'] = "Arizona"
        elif (metro.at[i, 'states_msa'] == "AR"):
            metro.at[i, 'states_msa'] = "Arkansas"
        elif (metro.at[i, 'states_msa'] == "CA"):
            metro.at[i, 'states_msa'] = "California"
        elif (metro.at[i, 'states_msa'] == "CO"):
            metro.at[i, 'states_msa'] = "Colorado"
        elif (metro.at[i, 'states_msa'] == "CT"):
            metro.at[i, 'states_msa'] = "Connecticut"
        elif (metro.at[i, 'states_msa'] == "DE"):
            metro.at[i, 'states_msa'] = "Delaware"
        elif (metro.at[i, 'states_msa'] == "FL"):
            metro.at[i, 'states_msa'] = "Florida"
        elif (metro.at[i, 'states_msa'] == "GA"):
            metro.at[i, 'states_msa'] = "Georgia"
        elif (metro.at[i, 'states_msa'] == "HI"):
            metro.at[i, 'states_msa'] = "Hawaii"
        elif (metro.at[i, 'states_msa'] == "ID"):
            metro.at[i, 'states_msa'] = "Idaho"
        elif (metro.at[i, 'states_msa'] == "IL"):
            metro.at[i, 'states_msa'] = "Illinois"
        elif (metro.at[i, 'states_msa'] == "IN"):
            metro.at[i, 'states_msa'] = "Indiana"
        elif (metro.at[i, 'states_msa'] == "IA"):
            metro.at[i, 'states_msa'] = "Iowa"
        elif (metro.at[i, 'states_msa'] == "KS"):
            metro.at[i, 'states_msa'] = "Kansas"
        elif (metro.at[i, 'states_msa'] == "KY"):
            metro.at[i, 'states_msa'] = "Kentucky"
        elif (metro.at[i, 'states_msa'] == "LA"):
            metro.at[i, 'states_msa'] = "Louisiana"
        elif (metro.at[i, 'states_msa'] == "ME"):
            metro.at[i, 'states_msa'] = "Maine"
        elif (metro.at[i, 'states_msa'] == "MD"):
            metro.at[i, 'states_msa'] = "Maryland"
        elif (metro.at[i, 'states_msa'] == "MA"):
            metro.at[i, 'states_msa'] = "Massachusetts"
        elif (metro.at[i, 'states_msa'] == "MI"):
            metro.at[i, 'states_msa'] = "Miami"
        elif (metro.at[i, 'states_msa'] == "MN"):
            metro.at[i, 'states_msa'] = "Minnesota"
        elif (metro.at[i, 'states_msa'] == "MS"):
            metro.at[i, 'states_msa'] = "Mississippi"
        elif (metro.at[i, 'states_msa'] == "MO"):
            metro.at[i, 'states_msa'] = "Missouri"
        elif (metro.at[i, 'states_msa'] == "MT"):
            metro.at[i, 'states_msa'] = "Motana"
        elif (metro.at[i, 'states_msa'] == "NE"):
            metro.at[i, 'states_msa'] = "Nebraska"
        elif (metro.at[i, 'states_msa'] == "NV"):
            metro.at[i, 'states_msa'] = "Nevada"
        elif (metro.at[i, 'states_msa'] == "NH"):
            metro.at[i, 'states_msa'] = "New Hampshire"
        elif (metro.at[i, 'states_msa'] == "NJ"):
            metro.at[i, 'states_msa'] = "New Jersey"
        elif (metro.at[i, 'states_msa'] == "NM"):
            metro.at[i, 'states_msa'] = "New Mexico"
        elif (metro.at[i, 'states_msa'] == "NY"):
            metro.at[i, 'states_msa'] = "New York"
        elif (metro.at[i, 'states_msa'] == "NC"):
            metro.at[i, 'states_msa'] = "North Carolina"
        elif (metro.at[i, 'states_msa'] == "ND"):
            metro.at[i, 'states_msa'] = "North Dakota"
        elif (metro.at[i, 'states_msa'] == "OH"):
            metro.at[i, 'states_msa'] = "Ohio"
        elif (metro.at[i, 'states_msa'] == "OK"):
            metro.at[i, 'states_msa'] = "Oklahoma"
        elif (metro.at[i, 'states_msa'] == "OR"):
            metro.at[i, 'states_msa'] = "Oregon"
        elif (metro.at[i, 'states_msa'] == "PA"):
            metro.at[i, 'states_msa'] = "Pennsylvania"
        elif (metro.at[i, 'states_msa'] == "RI"):
            metro.at[i, 'states_msa'] = "Rhode Island"
        elif (metro.at[i, 'states_msa'] == "SC"):
            metro.at[i, 'states_msa'] = "South Carolina"
        elif (metro.at[i, 'states_msa'] == "SD"):
            metro.at[i, 'states_msa'] = "South Dakota"
        elif (metro.at[i, 'states_msa'] == "TN"):
            metro.at[i, 'states_msa'] = "Tennessee"
        elif (metro.at[i, 'states_msa'] == "TX"):
            metro.at[i, 'states_msa'] = "Texas"
        elif (metro.at[i, 'states_msa'] == "UT"):
            metro.at[i, 'states_msa'] = "Utah"
        elif (metro.at[i, 'states_msa'] == "VT"):
            metro.at[i, 'states_msa'] = "Vermont"
        elif (metro.at[i, 'states_msa'] == "VA"):
            metro.at[i, 'states_msa'] = "Virginia"
        elif (metro.at[i, 'states_msa'] == "WA"):
            metro.at[i, 'states_msa'] = "Washington"
        elif (metro.at[i, 'states_msa'] == "WV"):
            metro.at[i, 'states_msa'] = "West Virginia"
        elif (metro.at[i, 'states_msa'] == "WI"):
            metro.at[i, 'states_msa'] = "Wisconsin"
        elif (metro.at[i, 'states_msa'] == "WY"):
            metro.at[i, 'states_msa'] = "Wyoming"
        elif (metro.at[i, 'states_msa'] == "PR"):
            metro.at[i, 'states_msa'] = "Puerto Rico"
        i += 1
    merged = metro.merge(covid, how='inner',
                         left_on=["states_msa", "name10_county"],
                         right_on=["state","county"])
    merged = merged[['date', 'county', 'cases',
                     'deaths', 'name_msa', 'states_msa_code', 'states_msa', 'states_msa_full',
                     'geoid_msa']]
    merged["date"] = pd.to_datetime(merged["date"])
    merged = merged[merged.date <= enddate]
    merged = merged[merged.date >= startdate]

    iterate_start = startdate

    interval_data = merged
    output = pd.DataFrame()

    while iterate_start <= enddate:
        iterate_end = iterate_start + timedelta(days=interval)

        eachInterval = interval_data[interval_data.date >= iterate_start]
        eachInterval = eachInterval[eachInterval.date <= iterate_end]


        eachInterval = eachInterval.groupby(['name_msa'])['cases', 'deaths'].sum()
        eachInterval = eachInterval.merge(metro_initial, left_on='name_msa', right_on='name_msa')[['states_msa_code', 'states_msa',
                                    'states_msa_full', "geoid_msa",
                                   'name_msa', 'cases', 'deaths']].sort_values(by = 'states_msa_code')
        eachInterval['interval_start'] = iterastart
        eachInterval = eachInterval.drop_duplicates(subset=['name_msa'])
        #print(eachInterval)
        output = output.append(eachInterval)
        iterate_start = iterate_start + timedelta(days=interval)

    #print(output)

    output.to_csv("output.csv", index = False)


# In[36]:


if __name__ == "__main__":

#     parser = argparse.ArgumentParser(description = 'Covid-19 data at MSA level')

#     parser.add_argument('--inputFile', type = str, default = "Covid-19 data(unsorted)")
#     parser.add_argument('--beginDate', type = str)
#     parser.add_argument('--beginDate', type = str)

    beginDate = dt.datetime(2020, 5, 2)
    endDate = dt.datetime(2020, 7, 23)
    interval = 7
    inputFile = 'Covid-19 cumulative.csv'
    inputMetro = 'metro_county.csv'
    # outputFile = 'Aggregated.csv'

    #data = cumulativeToDaily(inputFile)
    dailyCount = cumulativeToDaily(inputFile)
    dailyCount.to_csv("daily count.csv", index = False)
    inputCovid = pd.read_csv("daily count.csv")

    aggregate(inputCovid, inputMetro, beginDate, endDate, interval)


# In[ ]:
