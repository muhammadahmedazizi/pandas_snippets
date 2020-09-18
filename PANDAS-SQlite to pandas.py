import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt

conn = sql.connect('weather.db')

weather = pd.read_sql('SELECT * FROM weather', conn)

print (weather)
