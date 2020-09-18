import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv('londonweather.csv')

#print (weather)

conn = sql.connect('weather.db')

weather.to_sql('weather', conn)



