# -*- coding: utf-8 -*-
"""Bike Sharing .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12nQvgKHUPixzHg3aAhK-SQ--IWhdbKOw

**Seoul Bike Sharing Demand
Donated on 2/29/2020**
link: https://archive.ics.uci.edu/dataset/560/seoul+bike+sharing+demand

**Dataset Information**
Additional Information

Currently Rental bikes are introduced in many urban cities for the enhancement of mobility comfort. It is important to make the rental bike available and accessible to the public at the right time as it lessens the waiting time. Eventually, providing the city with a stable supply of rental bikes becomes a major concern. The crucial part is the prediction of bike count required at each hour for the stable supply of rental bikes.
The dataset contains weather information (Temperature, Humidity, Windspeed, Visibility, Dewpoint, Solar radiation, Snowfall, Rainfall), the number of bikes rented per hour and date information.
"""

from google.colab import drive
from IPython.display import Image
upload = files.upload()

drive.mount('/content/drive')

Image("data.jpg")

"""Importing pandas and numpy"""

import pandas as pd
import numpy as np

import chardet

with open('SeoulBikeData.csv', 'rb') as f:
    result = chardet.detect(f.read())  # or readline if the file is large
#first failed to read the initial encoding, this code helped from stackoverflow https://stackoverflow.com/questions/33819557/unicodedecodeerror-utf-8-codec-while-reading-a-csv-file

data = pd.read_csv('SeoulBikeData.csv', encoding=result['encoding'])

"""Data Set successfully Loaded

"""

data.head()

data.info()

#count of missing values in each column.
data.isna().sum()

"""This dataset has 14 features (columns) and 8760 rows.

'Rented Bike Count' is the key attribute for this set

The data does not have any null values
"""

# Checking Duplicate Values
duplicates =len(data[data.duplicated()])
print(duplicates)

data.describe()

"""**QUESTIONS WE HAVE TO ANSWER**

1. What are we trying to predict ?
2. Which season has the most rentals ?
3. In which month or day are most rentals ?
4. Which attribute has the biggest effect on our variable?

# **Exploratory Data Analysis**
"""

import matplotlib.pyplot as plt
import seaborn as sb

sb.boxplot(x='Seasons', y='Rented Bike Count', data=data)
plt.show()

import datetime as dt
#data['Date'] = data['Date'].apply(lambda x: dt.datetime.strptime(x,"%d/%m/%Y"))
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

data['year'] = data['Date'].dt.year
data['month'] = data['Date'].dt.month

data['day'] = data['Date'].dt.day_name()

plt.bar(x='year', height='Rented Bike Count', data=data, color ='green', )

plt.xlabel(" Rented Bike")
plt.ylabel(" Year ")
plt.title("No. of Rented Bike Count")
plt.show()

sb.violinplot(data=data, x='day', y='Rented Bike Count') # Comparing days
plt.xticks(rotation=15);
plt.show()
sb.violinplot(data=data, x='Seasons', y='Rented Bike Count') # Comparing seasons
plt.xticks(rotation=15);
plt.show()

sb.violinplot(data=data, x='Seasons', y='Rented Bike Count') # Changed 'season' to 'Seasons'
plt.xticks(rotation=15);
plt.show()

"""Summer is the peak season"""

