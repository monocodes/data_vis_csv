import csv
from datetime import datetime

from matplotlib import pyplot as plt

def convert_temp(temp_f):
    """converts fahrenheit to celsius"""
    temp_c = (temp_f - 32)*5/9
    return temp_c

def get_weather_data(
    filename, dates, highs, lows, date_index,
    high_index, low_index):
    """Get the highs and lows from a data file."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get Dates, and high and low temperatures from this file.
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                high = convert_temp(high)
                low = int(row[low_index])
                low = convert_temp(low)
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# Get weather data for Sitka
filename = 'data/sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(
    filename, dates, highs, lows, date_index=2,
    high_index=5, low_index=6)

# Plot Sitka weather data.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(13, 7))
ax.plot(dates, highs, c='red', alpha=0.75)
ax.plot(dates, lows, c='blue', alpha=0.75)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.30)

# Get weather data for Death Valley.
filename = 'data/death_valley_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(
    filename, dates, highs, lows, date_index=2,
    high_index=4, low_index=5)

# Add Death Valley data to current plot.
ax.plot(dates, highs, c='yellow', alpha=0.3)
ax.plot(dates, lows, c='black', alpha=0.3)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

# Get weather data for San Francisco.
filename = 'data/san_francisco_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(
    filename, dates, highs, lows, date_index=2,
    high_index=5, low_index=6)

# Add San Francisco data to current plot.
ax.plot(dates, highs, c='purple', alpha=0.5)
ax.plot(dates, lows, c='green', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# Format plot.
title = "Daily high and low temperatures - 2018"
title += "\nSitka, AK; Death Valley, CA; San Francisco, CA"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (C)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(-10, 60)

plt.show()