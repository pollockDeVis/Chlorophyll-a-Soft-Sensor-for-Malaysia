# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:39:49 2021

@author: Pollock
"""

#Importing Libraries
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

#Reading excel file and converting date time to pandas datetime format
df1 = pd.read_excel('dataset/lake_dataset_raw.xlsx', converters={'Date Time': pd.to_datetime})
df1 = df1.rename(columns={'Date Time' : 'datetime', 'Actual Conductivity (µS/cm) (624571)' : 'actual_conductivity',
       'Specific Conductivity (µS/cm) (624571)' : 'specific_conductivity',
       'Total Dissolved Solids (ppt) (624571)' : 'total_dissolved_solids',
       'RDO Concentration (mg/L) (543925)': 'do_concentration', 'RDO Saturation (%Sat) (543925)': 'do_saturation',
       'Oxygen Partial Pressure (Torr) (543925)' : 'oxygen_partial_pressure', 'Turbidity (NTU) (607780)': 'turbidity',
       'Chlorophyll-a Fluorescence (RFU) (622895)': 'chl-a_fluorescence',
       'Chlorophyll-a Concentration (µg/L) (622895)': 'chl-a_concentration',
       'Temperature (°C) (606143)': 'temperature'})




#plt.scatter(df1['chl-a_fluorescence'], df1['chl-a_concentration']) #[linear relationship]
#plt.scatter(df1['actual_conductivity'], df1['specific_conductivity']) #linear relationship
#plt.scatter(df1['do_concentration'], df1['do_saturation']) #linear relationship
#plt.scatter(df1['do_concentration'], df1['oxygen_partial_pressure']) #linear relationship
#plt.scatter(df1['turbidity'], df1['total_dissolved_solids']) #nonlinear 
#plt.scatter(df1['total_dissolved_solids'], df1['chl-a_concentration'])


#dropping non-useful columns 

df1 = df1.drop(columns= ['specific_conductivity', 'total_dissolved_solids', 'do_saturation', 'oxygen_partial_pressure', 'chl-a_fluorescence'])

#setting datetime as the index and sorting the dataframe
df1 = df1.set_index('datetime').sort_index()

#Missing value info
missing_summary= df1.isna().sum()
#missing_summary.plot(kind='bar')
df1 = df1.dropna()

#df1['do_concentration'].hist() #normal distribution
#df1['chl-a_concentration'].hist()
#df1['temperature'].hist() #normal distribution
#df1['actual_conductivity'].hist(bins=50)
#df1['turbidity'].hist(bins=50)
#plt.show()

#Outlier detection
#turbidity (low and high outliers) #actual conductivity low outlier
#temp, do_conc & chl-a_conc no oulier
#sns.boxplot(x=df1['do_concentration'])

#calculating z-score and removing outliers
abs_z_scores = np.abs(stats.zscore(df1))
filtered_entries= (abs_z_scores<3).all(axis=1)
new_df = df1[filtered_entries]
new_df.to_csv("cleaned_lake_dataset.csv")
#print(np.where(z>4))
