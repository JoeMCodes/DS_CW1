### This file will create the relavent data from the Pleiades_df.csv and create Figure-1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

df = pd.read_csv(r'./data/derived/Pleiades_df.csv')
df.loc[df['Description'].isna(), 'Description'] = 'Missing'
df = df.dropna()

## Here we are getting all data entries that have 'roman' in the title or
## 'a roman' in the discription, we take the article a to ensure the description references a roman thing as supposed to 'This Town would trade with the roman town nearby' 
Roman_title = df[df['Title'].str.lower().str.contains('roman ')]
Roman_decri = df[df['Description'].str.lower().str.contains('a roman ')]

roman_df = pd.merge(Roman_title, Roman_decri, how = 'outer')


### Coordinates for plotting 
lons_destroyed = roman_df[(roman_df['Start_Date']<=117) & (roman_df['End_Date']<=480)]['long']
lats_destroyed = roman_df[(roman_df['Start_Date']<=117) & (roman_df['End_Date']<=480)]['lat']
lons_survived = roman_df[(roman_df['Start_Date']<=117) & (roman_df['End_Date']>=480)]['long']
lats_survived = roman_df[(roman_df['Start_Date']<=117) & (roman_df['End_Date']>=480)]['lat']
lons_created = roman_df[(roman_df['Start_Date']>=117) & (roman_df['End_Date']>=480)]['long']
lat_created = roman_df[(roman_df['Start_Date']>=117) & (roman_df['End_Date']>=480)]['lat']


######## THIS CREATES THE PLOT

fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree()) ## CAN change type of projection

### This plots the map plot


ax.add_feature(cfeature.LAND, color = '#B7C6CF', zorder = 1)
ax.add_feature(cfeature.BORDERS, color = 'white', zorder = 2)


ax.scatter(lons_survived, lats_survived, s=5 , c ='#3EBCD2', linewidths = 0 ,transform=ccrs.PlateCarree(), zorder = 3, alpha = 0.5)
ax.scatter(lons_destroyed, lats_destroyed, s=5,c ='#A81829', linewidths = 0 ,transform=ccrs.PlateCarree(), zorder = 4, alpha = 0.5)
ax.scatter(lons_created, lat_created, s=5, c ='#EBB434', linewidths = 0 ,transform=ccrs.PlateCarree(), zorder = 5, alpha = 0.5)
ax.axis('off')
ax.set_extent([-10, 42, 57, 29], crs=ccrs.PlateCarree())


# Add in line and tag
ax.plot([0.12, .9],                 # Set width of line
        [1.0, 1.0],                # Set height of line
        transform=fig.transFigure,   # Set location relative to plot
        clip_on=False, 
        color='#E3120B', 
        linewidth=.6)
ax.add_patch(plt.Rectangle((0.12,1.0),                # Set location of rectangle by lower left corder
                           0.04,                       # Width of rectangle
                           -0.02,                      # Height of rectangle. Negative so it goes down.
                           facecolor='#E3120B', 
                           transform=fig.transFigure, 
                           clip_on=False, 
                           linewidth = 0))



# Add in title and subtitle
ax.text(x=0.12, y=.94, s="The Rise and Fall", transform=fig.transFigure, ha='left', fontsize=13, weight=700, fontfamily = 'Sans')
ax.text(x=0.12, y=.905, s="Destruction and Creation of Roman \'Places\' in 117 CE compared to 480 CE", transform=fig.transFigure, ha='left', fontsize=11,weight = 400, fontfamily="Sans")

# Set source text
ax.text(x=0.12, y=.12, s="""Source: "Ancient roman places from Pleiades dataset" via pleiades.stoa.org""", transform=fig.transFigure, ha='left', fontsize=9, weight = 300, alpha=.75)

## ADD legend

ax.add_patch(plt.Rectangle((0.12,0.87),                # Set location of rectangle by lower left corder
                           0.03,                       # Width of rectangle
                           0.02,                      # Height of rectangle. Negative so it goes down.
                           facecolor='#3EBCD2', 
                           transform=fig.transFigure, 
                           clip_on=False, 
                           linewidth = 0))
ax.add_patch(plt.Rectangle((0.24,0.87),                # Set location of rectangle by lower left corder
                           0.03,                       # Width of rectangle
                           0.02,                      # Height of rectangle. Negative so it goes down.
                           facecolor='#A81829', 
                           transform=fig.transFigure, 
                           clip_on=False, 
                           linewidth = 0))
ax.add_patch(plt.Rectangle((0.37,0.87),                # Set location of rectangle by lower left corder
                           0.03,                       # Width of rectangle
                           0.02,                      # Height of rectangle. Negative so it goes down.
                           facecolor='#EBB434', 
                           transform=fig.transFigure, 
                           clip_on=False, 
                           linewidth = 0))

ax.text(x=0.155, y=.87, s="Survived", transform=fig.transFigure, ha='left', fontsize=11,weight = 400, fontfamily="Sans")
ax.text(x=0.275, y=.87, s="Destroyed", transform=fig.transFigure, ha='left', fontsize=11,weight = 400, fontfamily="Sans")
ax.text(x=0.405, y=.87, s="Created", transform=fig.transFigure, ha='left', fontsize=11,weight = 400, fontfamily="Sans")





plt.savefig(r'./outputs/figures/figure-1.svg', bbox_inches = 'tight', facecolor = 'white')