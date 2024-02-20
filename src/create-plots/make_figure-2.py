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

### MAKE THE PLOT

Category = ['27 BCE', '117 CE', '480 CE']

fig, ax1 = plt.subplots(figsize=(6, 6))


X = np.arange(3)
ax2 = ax1.twinx()


ax1.bar(X-0.15, [no_places_27bc, no_places_117, no_places_480], color = '#3EBCD2', width = 0.3, zorder = 2)
ax2.bar(X+0.15, [no_roman_places_27bc, no_roman_places_117, no_roman_places_480], color = '#A81829', width = 0.3, zorder = 2)
ax1.set_xlim(-1,3)


ax1.grid(which="major", axis='y', color='#758D99', alpha=0.6, zorder=1)

# Remove splines
ax1.spines[['top','left', 'right']].set_visible(False)

# Make left spine slightly thicker
ax1.spines[['bottom']].set_linewidth(1.1)

ax2.spines[['top','left', 'right']].set_visible(False)

# Set custom labels for y-axis
ax1.set_yticks([0,5000,10000,15000,20000])
ax1.set_yticklabels([0,5,10,15,20], color = '#3EBCD2',
                    ha = 'left',
                    verticalalignment = 'bottom')

## Hacky scaling - The labels are not %100 accurate but the difference is very small (just a difference of 2)
## We scale like this so the two scales match up
ax2_scale = (5000/no_places_117)*no_roman_places_117
ax2.set_yticks([0,ax2_scale,ax2_scale*2,ax2_scale*3,ax2_scale*4])
ax2.set_yticklabels([0,3,6,9,12], color = '#A81829',
                    ha = 'right',
                    verticalalignment='bottom')

# Reformat y-axis tick labels
ax1.yaxis.set_tick_params(labelleft=True,      # Put x-axis labels on left
                         labelright=False,  # Set no x-axis labels on right
                         left=False,       # Set no ticks on left
                         labelsize=11,       # Set tick label size
                         pad=-1)             # Lower tick labels a bit

ax2.yaxis.set_tick_params(labelleft=False,      # Set no x-axis labels on left
                         labelright=True,  # put x-axis labels on right
                         right=False,       # Set no ticks on right
                         labelsize=11,       # Set tick label size
                         pad=-1)             # Lower tick labels a bit

plt.xticks(X, Category) 
ax1.xaxis.set_tick_params(bottom = False, labelsize = 11, pad = 1)

# Add in line and tag
ax2.plot([0.12, .91],                  # Set width of line
        [1.00, 1.00],                  # Set height of line
        transform=fig.transFigure,   # Set location relative to plot
        clip_on=False, 
        color='#E3120B', 
        linewidth=.6)
ax1.add_patch(plt.Rectangle((0.12,1.00),                 # Set location of rectangle by lower left corder
                           0.04,                       # Width of rectangle
                           -0.02,                      # Height of rectangle. Negative so it goes down.
                           facecolor='#E3120B', 
                           transform=fig.transFigure, 
                           clip_on=False, 
                           linewidth = 0))

# Add in title and axis titles
ax1.text(x=0.12, y=.945, s="The Destruction of Roman Places", transform=fig.transFigure, ha='left', fontsize=13, weight=700, fontfamily = 'Sans')
ax1.text(x=0.12, y=.87, s="Number of Ancient \'places\' \n'000",color ='#3EBCD2', transform=fig.transFigure, ha='left', weight = 400, fontsize=11, fontfamily = 'Sans')
ax1.text(x=0.91, y=.87, s="Number of Roman \'places\'\n'00",color ='#A81829', transform=fig.transFigure, ha='right', weight = 400, fontsize=11, fontfamily = 'Sans')


# Set source text
ax1.text(x=0.12, y=.05, s="""Source: "Ancient places from Pleiades dataset" via pleiades.stoa.org""", transform=fig.transFigure, ha='left', fontsize=9, alpha=.75)

plt.savefig(r'./outputs/figures/figure-2.svg', bbox_inches = 'tight', facecolor = 'white')