# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 00:11:51 2021

@author: Pollock
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
'''
import datetime

import numpy as np
'''

dataset = pd.read_csv('2021_10_24_cleaned_lake_dataset.csv', header=0, index_col=0)
values = dataset.values

#Visualization of Subplots
groups = [0,1,2,3,4]
colors=['purple', 'blue', 'orange', 'green',  'red']
column_names = ['conductivity', 'do', 'turbidity', 'chl-a', 'temperature']
i = 1

plt.figure()
for group  in groups:
    plt.subplot(len(groups), 1, i)
    plt.plot(values[:,group], color = colors[i-1])
    plt.title(dataset.columns[group], x=0.01, y=0.65, loc='left', fontsize = 10)
    i += 1
plt.show()

#Preprocessing Data

#Ascertain all data is float
values = values.astype('float32')

#Normalizing Features
scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(values)
scaled_df = pd.DataFrame(scaled_data)

#Train-Test Split

values = scaled_df.values
n_train = 7516             #leaving 1000 data points for testing
train = values[:n_train, :]
test = values[n_train:,:]

train_X = train[:,[0,1,2,4]]
train_y = train[:,3]

test_X = test[:,[0,1,2,4]]
test_y = test[:,3]

#




















