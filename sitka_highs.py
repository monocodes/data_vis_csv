from asyncore import read
import csv

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
    
print(highs)