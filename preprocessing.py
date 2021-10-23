# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 21:39:49 2021

@author: Pollock
"""

#Importing Libraries
import pandas as pd
import datetime
import matplotlib.pyplot as plt

#Reading excel file and converting date time to pandas datetime format
df1 = pd.read_excel('dataset/lake_dataset_raw.xlsx', converters={'Date Time': pd.to_datetime})
df1 = df1.rename(columns={'Date Time' : 'datetime', 'Actual Conductivity (µS/cm) (624571)' : 'actual_conductivity',
       'Specific Conductivity (µS/cm) (624571)' : 'specific_condictivity',
       'Total Dissolved Solids (ppt) (624571)' : 'total_dissolved_solids',
       'RDO Concentration (mg/L) (543925)': 'do_concentration', 'RDO Saturation (%Sat) (543925)': 'do_saturation',
       'Oxygen Partial Pressure (Torr) (543925)' : 'oxygen_partial_pressure', 'Turbidity (NTU) (607780)': 'turbidity',
       'Chlorophyll-a Fluorescence (RFU) (622895)': 'chl-a_fluorescence',
       'Chlorophyll-a Concentration (µg/L) (622895)': 'chl-a_concentration',
       'Temperature (°C) (606143)': 'temperature'})
#Missing value info
missing_summary= df1.isna().sum()
missing_summary.plot(kind='bar')

plt.show()