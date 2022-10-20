import csv

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
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
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(13, 7))
ax.plot(highs, c='red')

# Format plot.
ax.set_title("Daily high temperatures, July 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()