import json, math, copy, sys
# from geosnap.io import store_ltdb
# from geosnap import Community, datasets
# from geosnap.io import store_census
import pandas as pd
import shapely.wkt
import shapely.geometry
from datetime import datetime
from datetime import timedelta
from pathlib import Path
import urllib.parse
import webbrowser
import os
import pprint
from sklearn.preprocessing import minmax_scale
import numpy as np
from scipy import stats
from notebook import notebookapp
from IPython.core.display import display, HTML
import geopandas as gpd
import argparse



"""

This function is for converting the output in csv format to js format 

"""

def convert_to_js(param):

    disease = param['Disease']
    beginDate = param['begin_date']
    endDate = param['end_date']
    shapefile = param['shapefile']
    
    with open(shapefile, errors='replace') as f:
        data = json.load(f)

    beginDate = str_to_date(beginDate)
    endDate = str_to_date(endDate)
    
    
    
    df = pd.read_csv(disease)
    
    
 
    columns = list(df.columns)
    columns.pop(0)
    columns.pop(0)
    
    for column in columns:
        column_date = str_to_date(column)
        if (column_date > endDate or column_date < beginDate):
            df = df.drop(column, 1)
            
    
    heading = list(df.columns)
    ofile = open('./data/test.js', 'w')
    ofile.write('var GEO_VARIABLES =\n')
    ofile.write('[\n')
    ofile.write('  '+json.dumps(heading)+',\n')
    
    for index, row in df.iterrows():
        values = list(row)
        ofile.write('  '+json.dumps(values)+',\n')
    
    
    ofile.write(']\n')
    ofile.close()

"""

Helper function for converting string to datetime, string must be in the formate of "month-date-year", e.g. "2-14-2020"


"""

def str_to_date(input_string):
    input_string = input_string.split('-')
    
    
    for index in range(len(input_string)):
        input_string[index] = int(input_string[index])

    input_string = dt.datetime(input_string[0], input_string[1], input_string[2])
    
    return input_string


"""

This function is for converting shapefile to geojson format 

"""
def write_GEO_JSON_js_test(param):    
    # read shape file to df_shape
    df_shapes = gpd.read_file(param['shapefile'])
    print(df_shapes.head())
    #print(type(df_shapes))
    df_shapes = df_shapes.rename(columns={'GEOID10': 'geoid'})
    

    
    geoid = df_shapes.columns[0]
    df_shapes = df_shapes[pd.notnull(df_shapes['geometry'])]
    
    # open GEO_JSON.js write heading for geojson format
    filename_GEO_JSON = "test1.js"
    ofile = open(filename_GEO_JSON, 'w')
    ofile.write('var GEO_JSON =\n')
    ofile.write('{"type":"FeatureCollection", "features": [\n')
    
    
    #Convert geometry in GEOJSONP to geojson format
    wCount = 0
    for shape in df_shapes.itertuples():
        feature = {"type":"Feature"}
        
        if (type(shape.geometry) is float):								# check is NaN?
            continue
            
        aShape = shapely.wkt.loads(str(shape.geometry))
        feature["geometry"] = shapely.geometry.mapping(aShape)

        
        #print(shape.__getattribute__)
        feature["properties"] = {geoid: shape.__getattribute__(geoid)}
        wCount += 1
        
        #print(feature)
        ofile.write(json.dumps(feature)+',\n')
    #print("GEO_JSON.js write count:", wCount)
    # complete the geojosn format by adding parenthesis at the end.	
    ofile.write(']}\n')
    ofile.close()
    



if __name__ == "__main__":
    
    
        
    param = {
        'Disease': './data/output_deaths.csv',  
        'begin_date': "2020-02-22",
        'end_date': "2020-06-10",
        'shapefile': "./shp/world_region.shp",
        'filename_suffix': "test1.js"
    }
    
    write_GEO_JSON_js_test(param)