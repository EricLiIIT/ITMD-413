'''
Author: Eric Li
A20419312
ITMD 413 - HW 14

This program uses various Python libraries to graph and demonstrate machine learning.
'''

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

file = pd.read_csv("ave_yearly_temp_nyc_1895-2017.csv")

def graph_1():
  cali = fetch_california_housing()
  ca_df = pd.DataFrame(cali.data, columns = cali.feature_names)
  g1 = sns.pairplot(data=ca_df, x_vars='MedInc', y_vars='AveRooms')
  #print(ca_df.columns)
  plt.show()

def graph_2():
  X_train, X_test, y_train, y_test = train_test_split(
    file.Date.values.reshape(-1, 1), file.Value.values,
    random_state=11)

  #print(X_train.shape)
  #print(X_test.shape)

  linear_regression = LinearRegression()
  linear_regression.fit(X=X_train, y=y_train)
  LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

  #print(linear_regression.coef_)
  #print(linear_regression.intercept_)

  predicted = linear_regression.predict(X_test)
  expected = y_test

  #for p, e in zip(predicted[::5], expected[::5]):
    #print(f'predicted: {p:.2f}, expected:{e:.2f}')

  predict = (lambda x: linear_regression.coef_ * x + linear_regression.intercept_)

  #print(predict(2019))
  #print(predict(1890))

  axes = sns.scatterplot(data=file, x='Date', y='Value', hue='Value', palette='winter', legend=False)
  axes.set_ylim(10, 70)

  x = np.array([min(file.Date.values), max(file.Date.values)])
  y = predict(x)

  line = plt.plot(x, y)

  plt.show()

graph_1()
graph_2()