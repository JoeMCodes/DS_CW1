### This file will create the relavent data from the Pleiades_df.csv and create Figure-2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'data/derived/Pleiades_df.csv')
df.loc[df['Description'].isna(), 'Description'] = 'Missing'
df = df.dropna() ## We are using the full dataset for this plot so we want to remove data entries with missing values


## Here we are getting all data entries that have 'roman' in the title or
## 'a roman' in the discription, we take the article a to ensure the description references a roman thing as supposed to 'This Town would trade with the roman town nearby' 

Roman_title = df[df['Title'].str.lower().str.contains('roman ')]
Roman_decri = df[df['Description'].str.lower().str.contains('a roman ')]
Roman_full = pd.merge(Roman_title, Roman_decri, how = 'outer') 

## Get the number of places for different dates
no_places_27bc =len(df[(df['Start_Date']<= -27)& (df['End_Date']>=-27)])
no_roman_places_27bc = len(Roman_full[(Roman_full['Start_Date']<= -27)& (Roman_full['End_Date']>=-27)])
no_places_117 =len(df[(df['Start_Date']<= 117)& (df['End_Date']>=117)])
no_roman_places_117 = len(Roman_full[(Roman_full['Start_Date']<= 117)& (Roman_full['End_Date']>=117)])
no_places_480 =len(df[(df['Start_Date']<= 480)& (df['End_Date']>=480)])
no_roman_places_480 = len(Roman_full[(Roman_full['Start_Date']<= 480)& (Roman_full['End_Date']>=480)])

### MAKE TEH PLOT

Category = ['27 BCE', '117 CE', '480 CE']

fig, ax1 = plt.subplots(figsize=(9, 6))


X = np.arange(3)
ax2 = ax1.twinx()
# ax1.set_ylim(0,20000)
# ax2.set_ylim(0,1600)
# ax2.set_xticks([0, 750,1500,2250,3000])
# ax2.set_xticklabels([0, 750,1500,2250,3000])

ax1.bar(X, [no_places_27bc, no_places_117, no_places_480], color = 'blue', width = 0.25)
ax2.bar(X+0.25, [no_roman_places_27bc, no_roman_places_117, no_roman_places_480], color = 'red', width = 0.25)

# Zorder tells it which layer to put it on. We are setting this to 1 and our data to 2 so the grid is behind the data.
ax1.grid(which="major", axis='y', color='#758D99', alpha=0.6, zorder=0)

# Remove splines. Can be done one at a time or can slice with a list.
ax1.spines[['top','left', 'right']].set_visible(False)

# Make left spine slightly thicker
ax1.spines[['bottom']].set_linewidth(1.1)
ax2.spines[['top','left', 'right']].set_visible(False)

# Reformat x-axis tick labels
ax1.yaxis.set_tick_params(labelleft=True,
                         left=False, 
                         labelsize=11, 
                         pad=-1)   
# Reformat x-axis tick labels
ax2.yaxis.set_tick_params(labelright=True,      # Put x-axis labels on top
                         right=False,       # Set no ticks on right
                         labelsize=11,       # Set tick label size
                         pad=-1)             # Lower tick labels a bit
