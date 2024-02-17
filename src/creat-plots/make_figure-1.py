### This file will create the relavent data from the Pleiades_df.csv and create Figure-1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

df = pd.read_csv(r'./data/derived/Pleiades_df.csv') ## Read in data frame
roman_df = df[df['Title'].str.lower().str.contains('roman ')] ## Create data frame of Roman 'tagged' places
roman_df = roman_df[roman_df['Start_Date']<500.0] ### No roman places are created after 500 AD


### Coordinates for plotting 
lons_117AD = roman_df[(roman_df['Start_Date']<=117) & (roman_df['End_Date']>=117)]['long']
lats_117AD = roman_df[(roman_df['Start_Date']<=117) & (roman_df['End_Date']>=117)]['lat']
lons_480AD = roman_df[(roman_df['Start_Date']<=480) & (roman_df['End_Date']>=480)]['long']
lats_480AD = roman_df[(roman_df['Start_Date']<=480) & (roman_df['End_Date']>=480)]['lat']
lons_both = roman_df[(roman_df['Start_Date']<=117) & (roman_df['End_Date']>=480)]['long']
lat_both = roman_df[(roman_df['Start_Date']<=117) & (roman_df['End_Date']>=480)]['lat']


######## THIS CREATES THE PLOT

fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree()) ## CAN change type of projection

### This plots the map plot

ax.add_feature(cfeature.LAND, color = '#B7C6CF', zorder = 1)
ax.add_feature(cfeature.BORDERS, color = 'white', zorder = 2)


ax.scatter(lons_117AD, lats_117AD, s=5 , c ='#3EBCD2' ,transform=ccrs.PlateCarree(), zorder = 3)
ax.scatter(lons_480AD, lats_480AD, s=5,c ='#A81829' ,transform=ccrs.PlateCarree(), zorder = 4)
ax.scatter(lons_both, lat_both, s=5, c ='#EBB434' ,transform=ccrs.PlateCarree(), zorder = 5)
ax.axis('off')
ax.set_extent([-10, 42, 57, 29], crs=ccrs.PlateCarree())


# Add in line and tag
ax.plot([0.12, .9],                 # Set width of line
        [1.02, 1.02],                # Set height of line
        transform=fig.transFigure,   # Set location relative to plot
        clip_on=False, 
        color='#E3120B', 
        linewidth=.6)
ax.add_patch(plt.Rectangle((0.12,1.02),                # Set location of rectangle by lower left corder
                           0.04,                       # Width of rectangle
                           -0.02,                      # Height of rectangle. Negative so it goes down.
                           facecolor='#E3120B', 
                           transform=fig.transFigure, 
                           clip_on=False, 
                           linewidth = 0))



# Add in title and subtitle
ax.text(x=0.12, y=.96, s="The Rise and Fall", transform=fig.transFigure, ha='left', fontsize=13, weight='bold', alpha=.8)
ax.text(x=0.12, y=.925, s="Roman \'Places\' in 117 CE vs 480 CE", transform=fig.transFigure, ha='left', fontsize=11, alpha=.8)

# Set source text
ax.text(x=0.12, y=.12, s="""Source: "Ancient roman places from Pleiades dataset" via pleiades.stoa.org""", transform=fig.transFigure, ha='left', fontsize=9, alpha=.75)

## ADD legend

ax.add_patch(plt.Rectangle((0.12,0.89),                # Set location of rectangle by lower left corder
                           0.03,                       # Width of rectangle
                           0.02,                      # Height of rectangle. Negative so it goes down.
                           facecolor='#3EBCD2', 
                           transform=fig.transFigure, 
                           clip_on=False, 
                           linewidth = 0))
ax.add_patch(plt.Rectangle((0.22,0.89),                # Set location of rectangle by lower left corder
                           0.03,                       # Width of rectangle
                           0.02,                      # Height of rectangle. Negative so it goes down.
                           facecolor='#A81829', 
                           transform=fig.transFigure, 
                           clip_on=False, 
                           linewidth = 0))
ax.add_patch(plt.Rectangle((0.32,0.89),                # Set location of rectangle by lower left corder
                           0.03,                       # Width of rectangle
                           0.02,                      # Height of rectangle. Negative so it goes down.
                           facecolor='#EBB434', 
                           transform=fig.transFigure, 
                           clip_on=False, 
                           linewidth = 0))

ax.text(x=0.155, y=.89, s="117 CE", transform=fig.transFigure, ha='left', fontsize=11, alpha=.8)
ax.text(x=0.255, y=.89, s="480 CE", transform=fig.transFigure, ha='left', fontsize=11, alpha=.8)
ax.text(x=0.355, y=.89, s="Both", transform=fig.transFigure, ha='left', fontsize=11, alpha=.8)

plt.savefig(r'./outputs/figures/figure-1.png', dpi = 400, bbox_inches = 'tight', facecolor = 'white')