## This function will create datasets for settlement and road types

import json
import pandas as pd
import convert_dates

with open('data/raw/pleiades-places-latest.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

data = json_data['@graph'] ## Data entries stores in the Value of the dictionary


df_list = [] ## We will create a list and convert to pd.df, this method takes considerably less time than appending df itself
for location in data:
    id = location['id']
    PlaceType = location['placeTypes'] ## Type of 'place'

    if location['reprPoint'] != None: ## Deals with data missing reprPoint     
        reprPoint = location['reprPoint'] ## Representative coordinate
    else: reprPoint = [None, None]

    ##The Following help us deal with entries with missing dates
    try: 
        dates = location['features'][0]['properties']['snippet'].split(';')[1].split('-')
        dates[0] = convert_dates.convert_date(dates[0])
        dates[1] = convert_dates.convert_date(dates[1])
    except Exception as e: dates = [None, None]

    if location['features'] != []: ## Deals with data with missing features
        if location['features'][0]['geometry'] != None: # This filters out data with missing coordinate values
            coords = location['features'][0]['geometry']['coordinates'] ## List of coords used for places like roads
        else: coords = None
    else: coords = None

    Title = location['title']

    row = [id, PlaceType, reprPoint[0], reprPoint[1], dates[0], dates[1], coords, Title]
    df_list.append(row)

Pleiades_df = pd.DataFrame(df_list, columns = ['id','Place_Type', 'long', 'lat', 'Start_Date', 'End_Date','Coords_List', 'Title']) 
Pleiades_df.to_csv(r'./data/derived/Pleiades_df.csv', index=False)



#############
#############


## The following is disused code -- DELETE AT END IF NOT USED


# settlement_data = [(location['id'], location['features'], location['reprPoint']) for location in data if location['placeTypes'] == ['settlement']] ## Extracts the features for settlement entries, We keep the ID so we can found out more information later

# road_data = [(location['id'], location['features']) for location in data if location['placeTypes'] == ['road']] ## Extracts the features for road entries


# settlement_df_list = [] ## We will create a list and convert to pd.df, this method takes considerably less time than appending df itself
# for entry in settlement_data:
#     if entry[1] != []:# This filters out data with missing feature values
#         if entry[2] != None: # This filters out data with missing coordinate values
            
#             ##The Following help us deal with entries with missing dates
#             try: 
#                 dates = entry[1][0]['properties']['snippet'].split(';')[1].split('-')
#                 dates[0] = convert_dates.convert_date(dates[0])
#                 dates[1] = convert_dates.convert_date(dates[1])
#             except Exception as e: dates = [None, None]


#             row = [entry[0], entry[2][0], entry[2][1], dates[0], dates[1], entry[1][0]['properties']['title']]
#             settlement_df_list.append(row)

# settlement_df = pd.DataFrame(settlement_df_list, columns = ['id', 'long', 'lat', 'Start_Date', 'End_Date', 'Title'])


# road_df_list = []
# road_df = pd.DataFrame(columns = ['id', 'coordinates', 'Start_Date', 'End_Date'])
# for entry in road_data:
#     if entry[1] != []:# This filters out data with missing feature values
#         if entry[1][0]['geometry'] != None: # This filters out data with missing coordinate values

#             ##The Following help us deal with entries with missing dates
#             try: 
#                 dates = entry[1][0]['properties']['snippet'].split(';')[1].split('-')
#                 dates[0] = convert_dates.convert_date(dates[0])
#                 dates[1] = convert_dates.convert_date(dates[1])
#             except Exception as e: dates = [None, None]

#             row = [entry[0], entry[1][0]['geometry']['coordinates'], dates[0], dates[1], entry[1][0]['properties']['title']]
#             road_df_list.append(row)

# road_df = pd.DataFrame(road_df_list, columns = ['id', 'coordinates', 'Start_Date', 'End_Date', 'Title'])

# settlement_df.to_csv(r'./data/derived/settlement_df.csv', index=False)
# road_df.to_csv(r'./data/derived/road_df.csv', index=False)

