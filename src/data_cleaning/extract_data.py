
import json
import pandas as pd
from convert_dates import convert_date

with open('data/raw/pleiades-places-latest.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

data = json_data['@graph'] ## Data entries stores in the Value of the dictionary


df_list = [] ## We will create a list and convert to pd.df, this method takes considerably less time than appending df itself
for location in data:
    id = location['id']
    PlaceType = location['placeTypes'] ## Type of 'place'
    Description = location['description']

    if location['reprPoint'] != None: ## Deals with data missing reprPoint     
        reprPoint = location['reprPoint'] ## Representative coordinate
    else: reprPoint = [None, None]

    ##The Following help us deal with entries with missing dates
    try: 
        dates = location['features'][0]['properties']['snippet'].split(';')[1].split('-')
        dates[0] = convert_date(dates[0])
        dates[1] = convert_date(dates[1])
    except Exception as e: dates = [None, None]

    if location['features'] != []: ## Deals with data with missing features
        if location['features'][0]['geometry'] != None: # This filters out data with missing coordinate values
            coords = location['features'][0]['geometry']['coordinates'] ## List of coords used for places like roads
        else: coords = None
    else: coords = None

    Title = location['title']

    row = [id, PlaceType, reprPoint[0], reprPoint[1], dates[0], dates[1], coords, Title, Description]
    df_list.append(row)

Pleiades_df = pd.DataFrame(df_list, columns = ['id','Place_Type', 'long', 'lat', 'Start_Date', 'End_Date','Coords_List', 'Title', 'Description']) 
Pleiades_df.to_csv(r'./data/derived/Pleiades_df.csv', index=False)

 