import urllib.request
import pandas as pd
import matplotlib.pyplot as plt

urll    =   'https://data.weather.gov.hk/weatherAPI/hko_data/regional-weather/latest_since_midnight_maxmin.csv'
urllib.request.urlretrieve(urll, 'data.csv')

file_name   =   'data.csv'
df          =   pd.read_csv(file_name)

xx      =   df['Automatic Weather Station']
yy      =   df['Maximum Air Temperature Since Midnight(degree Celsius)']
zz      =   df['Minimum Air Temperature Since Midnight(degree Celsius)']

plt.bar(xx, yy)
plt.bar(xx, zz)
plt.show()