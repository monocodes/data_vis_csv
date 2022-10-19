import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, columb_header in enumerate(header_row):
        print(index, columb_header)