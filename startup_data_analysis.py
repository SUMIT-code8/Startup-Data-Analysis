# -*- coding: utf-8 -*-
"""Startup Data Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bLDs2zKv8yKNcWNZS8ON8PU6HhRspz5A
"""

import numpy as np
 import pandas as pd
 from numpy import math
 from sklearn.preprocessing import MinMaxScaler
 from sklearn.model_selection import train_test_split
 from sklearn.linear_model import LinearRegression
 from sklearn.metrics import r2_score
 from sklearn.metrics import mean_squared_error
 import matplotlib.pyplot as plt

dataset=pd.read_csv('50_Startups.csv')

len(dataset)

dataset.info()

dataset.head(10)

plt.scatter(dataset['Marketing Spend'], dataset['Profit'], alpha=0.5)
 plt.title('Scatter plot of Profit with Marketing Spend')
 plt.xlabel('Marketing Spend')
 plt.ylabel('Profit')
 plt.show()

plt.scatter(dataset['R&D Spend'], dataset['Profit'], alpha=0.5)
plt.title('Scatter plot of Profit with R&d Spend')
plt.xlabel('R&D Spend')
plt.ylabel('Profit')
plt.show()

plt.scatter(dataset['Administration'], dataset['Profit'], alpha=0.5)
plt.title('Scatter plot of Profit with administration Spend')
plt.xlabel('Administration')
plt.ylabel('Profit')
plt.show()

plt.scatter(dataset['R&D Spend'], dataset['Administration'], alpha=0.5)
plt.title('Scatter plot of R&D spend with administration ')
plt.xlabel('R&D Spend')
plt.ylabel('Administration')
plt.show()

plt.scatter(dataset['R&D Spend'], dataset['Marketing Spend'], alpha=0.5)
plt.title('Scatter plot of R&D spend with administration ')
plt.xlabel('R&D Spend')
plt.ylabel('Marketing Spend')
plt.show()

ax = dataset.groupby(['State'])['Profit'].mean().plot.bar(figsize = (10,5),fontsize = 14)
 ax.set_title("Average profit for different states where the startups operate", fontsize = 20)
 ax = dataset.groupby(['State'])['Profit'].mean().plot.bar(figsize = (10,5),fontsize = 14)
 ax.set_title("Average profit for different states where the startups operate", fontsize = 20)

 ax.set_xlabel("State", fontsize = 15)
 ax.set_ylabel("Profit", fontsize = 15)

dataset.State.value_counts()

dataset['NewYork_State'] = np.where(dataset['State']=='New York', 1, 0)
 dataset['California_State'] = np.where(dataset['State']=='California', 1, 0)
 dataset['Florida_State'] = np.where(dataset['State']=='Florida', 1, 0)
 # Drop the original column State from the dataframe
 dataset.drop(columns=['State'],axis=1,inplace=True)
 dataset.head()

dependent_variable = 'Profit'

independent_variables = list(set(dataset.columns.tolist()) - {dependent_variable})
independent_variables

X = dataset[independent_variables].values
 y = dataset[dependent_variable].values
 dataset[independent_variables]

#splitting the data set into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

X_train[0:10]

scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train[0:10]

regressor = LinearRegression()
regressor.fit(X_train, y_train)

regressor.intercept_

regressor.coef_

y_pred_train = regressor.predict(X_train)
 y_train

y_pred = regressor.predict(X_test)

mean_squared_error(y_test, y_pred)

math.sqrt(mean_squared_error(y_train, y_pred_train))

r2_score(y_train, y_pred_train)

r2_score(y_test, y_pred)