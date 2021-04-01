'''
Author: Eric Li
A20419312
ITMD 413
HW 11

This program will demonstrate the use of the Seaborn library with different figures and data sets built into the Seaborn library.
'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#import numpy as np

tips = sns.load_dataset("tips")
flights_data = pd.read_csv('flightsData.csv')
titanic = sns.load_dataset("titanic")
#tips = pd.read_csv("workerstips.csv") # Look for dataset names at GitHub link at the bottom of the code
#pd.set_option('display.max_columns', None)

def a(): # Part a
  a = sns.scatterplot(x="total_bill", y="tip", data=tips)
  plt.show()

def b(): # Part b
  b = sns.scatterplot(x="total_bill", y="tip", hue="smoker", style="smoker", data=tips) # part b
  plt.show()

def c(): # Part c
  c = sns.barplot(x='day', y='tip', data=tips)
  plt.show()

def d(): # Part d
  d = sns.boxplot(x='day', y='tip', hue="time", data=tips)
  plt.show()

def e(): # Part e
  # Collects value of average passengers per flight per year per month?
  monthly_passengers = flights_data.groupby('year').agg({'passengers':'mean'})
  monthly_passengers.insert(1, "avg", ["Monthly","Monthly","Monthly", "Monthly", "Monthly",
  "Monthly", "Monthly", "Monthly", "Monthly", "Monthly", "Monthly", "Monthly"]) # Gives criteria to distinguish dataframes

  yearly_passengers = flights_data.groupby('year').sum() # Collects annual sum of passengers
  yearly_passengers.insert(1, "avg", ["Yearly", "Yearly", "Yearly", "Yearly", "Yearly",
  "Yearly", "Yearly", "Yearly", "Yearly", "Yearly", "Yearly", "Yearly"])

  #print(monthly_passengers) # Dataframe type
  #print(yearly_passengers) # Dataframe type
  concat_df = [monthly_passengers, yearly_passengers] # Combines aggregated dataframes
  concat_graph = pd.concat(concat_df)
  #print(concat_graph.reset_index())
  ax = sns.lineplot(x='year', y='passengers', hue='avg', data=concat_graph)
  plt.show()

def f():
  #titanic["who"] = "" # Creates new empty column
  #titanic["who"] = np.where(titanic['Age'] < 18, "child", (np.where(titanic['Age'] > 18, "male", "female")))

  #titanic["who"] = np.where(titanic['Age'] < 18, "child", "")
  #titanic["who"] = np.where(titanic['Age'] > 18, "male", "")
  #titanic["who"] = np.where(titanic['who'] == "", "female", "female")
  #titanic["who"] = np.where(titanic['Sex'] == "female" & (np.where(titanic['Age'] > 18, "female", "male")))
  #print(titanic.head(50))

  #sns.catplot(x='class', y='Sex', col='survived', data=titanic, kind='bar')
  #plt.show()

  g = sns.catplot(x="class", hue="who", col="survived",
                  data=titanic, kind="count",
                  height=4, aspect=.7);
  plt.show()

def main():
  a()
  b()
  c()
  d()
  e()
  f()

main()

'''
Extras:

avg = tips.groupby("day").mean() # Prints averages for each day
avg_tip_sat = tips.loc['Sat']
avg_tip_fri = tips.loc[tips["day"] == "Fri"].mean().iloc[[1]] # Takes average tip from certain day (Friday)
avg_tip_sat = tips.loc[tips["day"] == "Sat"].mean().iloc[[1]] # Saturday
avg_tip_sun = tips.loc[tips["day"] == "Sun"].mean().iloc[[1]] # Sunday
avg_tip_thur = tips.loc[tips["day"] == "Thur"].mean().iloc[[1]] # Thursday
plt.show()
print(avg_tip_fri)
print(avg_tip_sat)
print(avg_tip_sun)
print(avg_tip_thur)
print(avg)

=== Helpful Sites ===

--> https://github.com/mwaskom/seaborn-data
    - contains names of ACTUAL data sets built into seaborn

https://medium.com/swlh/quick-guide-to-labelling-data-for-common-seaborn-plots-736e10bf14a9
https://seaborn.pydata.org/generated/seaborn.lineplot.html
https://pandas.pydata.org/docs/user_guide/merging.html Merging dataframes
https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html Dataframes
https://seaborn.pydata.org/tutorial/relational.html
https://seaborn.pydata.org/generated/seaborn.catplot.html Seaborn catplot
https://github.com/mwaskom/seaborn-data Seaborn data
'''