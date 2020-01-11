import os
import time

import pandas

while True:
    if os.path.exists('temps-today.csv'):
        data = pandas.read_csv('temps-today.csv')
        print(data.mean()["st1"])
    else:
        print("File doesn't exist")
    time.sleep(10)
