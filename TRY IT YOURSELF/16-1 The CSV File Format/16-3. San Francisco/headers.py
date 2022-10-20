import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/san_francisco_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)

    # get the first line of the file
    header_row = next(reader)

    # printing the headers and their positions
    for index, columb_header in enumerate(header_row):
        print(index, columb_header)