# Covid_MSA_code
This is a simple python program that can be run on Jupyternotebook to produce the Covid-19 data at the MSA level in the US. **COVID_aggregate_by_date** is the main python 
file used to generate the output. In the main function of the file, you can specify the start date, end date, and interval for the output. Specifying start date and end date
allows you the see the data only wthin a specific range of time. Interval, inputting as days, allow you to see the cases and deaths in each MSA only within each chunk of days.
For example, if your interval is one, then that means you will see the daily count of cases and deaths in each MSA.  
- Input data : **Covid-19 cumulative.csv** is the dataset that is maintained by the New York Times that has the cumulative Covid-19 data at county level. 
- Input data: **metro_county.csv** has the information on all the MSAs in the USA and which counties belong to them. This file should be left unchanged.
- Output data: **output.csv** is the output which has the Covid-19 cases and deaths at the MSA level. The "group" column specifies the exact date for which the count begins.
- There are some other files in the folder as well. **daily_count.csv** allows you to see the count at each day (since the original data is cumulative). **test.py** is a simple
program which can show you a graph of how Covid-19 cases at a MSA changes over time.
             
