# Covid_MSA_code
This is a simple python program that can be run on Jupyter Notebook to produce the Covid-19 data at the MSA level in the US. **COVID_aggregate_by_date** is the main python 
file used to generate the output. In the main function of the file, you can specify the start date, end date, and interval for the output. Specifying start date and end date
allows you the see the data only wthin a specific range of time. Interval, inputting as days, allow you to see the cases and deaths in each MSA only within each chunk of days.
For example, if your interval is one, then that means you will see the daily count of cases and deaths in each MSA.  
- Input data : **Covid-19 cumulative.csv** is the dataset published by the New York Times that has the cumulative Covid-19 data at county level every day. The data is maintained and organized by Dr. Zhiyu Li and can be found at https://wherecovid19.cigi.illinois.edu/data-info.html.   
- Input data: **metro_county.csv** has the information on all the MSAs in the USA and which counties belong to them. This file should be left unchanged.
- Output data: **output.csv** is the output which has the Covid-19 cases and deaths at the MSA level. Each row in the output is a record of how many new cases and deaths have occurred for a MSA within a time interval. **output_cases.csv** and **output_deaths.csv** are the transposed versions of output_cases.csv and contain the number of new cases and deaths at each MSA respectively.
- There are some other files in the folder as well. **daily_count.csv** allows you to see the count at each day (since the original data is cumulative). **test.py** is a simple
program which you can use to output a graph of how Covid-19 cases at a MSA changes over time.

## MSA_travel_aggregate
The folder MSA_travel_aggregate contains a script "travel_aggregate.py" which takes the dataset of travelers to each city produced by Bin as the input and outputs a dataset of travelers to each MSA in the US. The file **output.csv** contains all the travels from February to June.
             
## model_prediction
This will be the script containing all the essential functionality for forecasting Covid-19 cases. This is work in progress but right now it has sample plots in which you can see how the number of Covid-19 cases correlate with the number of travelers to a metropolitan area. Currently working on a neural network model.

## User Guide for data preprocessing
The main file that you need to run the code is in **COVID_aggregate_by_date.ipynb**, you can run it in **Jupyter Notebook** 

In the main funciton in the file, you will see a place where you can specify the beginning date and ending date:
![image](https://user-images.githubusercontent.com/47130002/101289826-5f7bd200-37c4-11eb-9330-3d7eb0d92c7d.png)


Additionaly you can change the time interval, i.e., if time_interval is 1 you get the daily count, or if it is 7 you get a weekly count:
![image](https://user-images.githubusercontent.com/47130002/101289875-b2ee2000-37c4-11eb-8bc0-eeb458a8eca7.png)

