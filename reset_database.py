import numpy as np
import pandas as pd
chart_data = pd.read_csv("raw_data.csv")
print(chart_data.columns)
for i in range(15):
    chart_data.iloc[i].iloc[1] = 0
complete_data = chart_data
print(complete_data)
complete_data.to_csv("line_chart.csv")

count = pd.read_csv('count.csv')
count = 0
print(count)