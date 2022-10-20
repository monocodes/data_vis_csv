### 16-1. Sitka Rainfall ###
"""
Sitka is in a temperate rainforest, so it gets a fair amount of rainfall. In the data file sitka_weather_2018_simple.csv is a header called PRCP, which represents daily rainfall amounts. Make a visualization focusing on the data in this column. You can repeat the exercise for Death Valley if you’re curious how little rainfall occurs in a desert.
"""

import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)

    # get the first line of the file
    header_row = next(reader)

    # printing the headers and their positions
    """
    for index, columb_header in enumerate(header_row):
        print(index, columb_header)
    """

    # list comprehension
    #highs = [int(row[5]) for row in reader]

    # Get dates and rainfall amounts from this file.
    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            prcp = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            prcps.append(prcp)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(13, 7))
ax.plot(dates, prcps, c='blue')

# Format plot.
title = "Daily rainfall amounts - Sitka, 2018"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall amounts", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()