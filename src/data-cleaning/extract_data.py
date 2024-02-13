## This function will create datasets for settlement and road types

import json
import pandas as pd
import convert_dates

with open('data/raw/pleiades-places-latest.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

data = json_data['@graph'] ## Data entries stores in the Value of the dictionary

settlement_data = [(location['id'], location['features']) for location in data if location['placeTypes'] == ['settlement']] ## Extracts the features for settlement entries, We keep the ID so we can found out more information later

road_data = [(location['id'], location['features']) for location in data if location['placeTypes'] == ['road']] ## Extracts the features for road entries

settlement_df_list = [] ## We will create a list and convert to pd.df, this method takes considerably less time than appending df itself
for entry in settlement_data:
    if entry[1] != []:# This filters out data with missing feature values
        if entry[1][0]['geometry'] != None: # This filters out data with missing coordinate values
            
            ##The Following help us deal with entries with missing dates
            try: 
                dates = entry[1][0]['properties']['snippet'].split(';')[1].split('-')
                dates[0] = convert_dates.convert_date(dates[0])
                dates[1] = convert_dates.convert_date(dates[1])
            except Exception as e: dates = [None, None]


            row = [entry[0], entry[1][0]['geometry']['coordinates'], dates[0], dates[1]]
            settlement_df_list.append(row)

settlement_df = pd.DataFrame(settlement_df_list, columns = ['id', 'coordinate', 'Start_Date', 'End_Date'])


road_df_list = []
road_df = pd.DataFrame(columns = ['id', 'coordinates', 'Start_Date', 'End_Date'])
for entry in road_data:
    if entry[1] != []:# This filters out data with missing feature values
        if entry[1][0]['geometry'] != None: # This filters out data with missing coordinate values

            ##The Following help us deal with entries with missing dates
            try: 
                dates = entry[1][0]['properties']['snippet'].split(';')[1].split('-')
                dates[0] = convert_dates.convert_date(dates[0])
                dates[1] = convert_dates.convert_date(dates[1])
            except Exception as e: dates = [None, None]

            row = [entry[0], entry[1][0]['geometry']['coordinates'], dates[0], dates[1]]
            road_df_list.append(row)

road_df = pd.DataFrame(road_df_list, columns = ['id', 'coordinates', 'Start_Date', 'End_Date'])

settlement_df.to_csv(r'./data/derived/settlement_df.csv', index=False)
road_df.to_csv(r'./data/derived/road_df.csv', index=False)

