'''
Author: Eric Li
A20419312
ITMD 413
Homework 9

Question 1
Write a program on the following two questions. Both Sections A and B should be written in one
program.
A (PANDAS: SERIES) Perform the following tasks with pandas Series:
a. Create a Series from the list [7, 11, 13, 17].
b. Create a Series with five elements that are all 100.0.
c. Create a Series with 20 elements that are all random numbers in the
range 0 to 100. Use method describe to produce the Series’ basic descriptive
statistics.
d. Create a Series called temperatures of the floating-point
values 98.6, 98.9, 100.2 and 97.9. Using the index keyword argument, specify
the custom indices 'Julie', 'Charlie', 'Sam' and 'Andrea'.
e. Form a dictionary from the names and values in Part (d), then use it to initialize
a Series.

B (PANDAS: DATAFRAMES) Perform the following tasks with pandas DataFrames:
f. Create a DataFrame named temperatures from a dictionary of three temperature
readings each for 'Maxine', 'James' and 'Amanda'.
g. Recreate the DataFrame temperatures in Part (a) with custom indices using
the index keyword argument and a list
containing 'Morning', 'Afternoon' and 'Evening'.
h. Select from temperatures the column of temperature readings for 'Maxine'.
i. Select from temperatures the row of 'Morning' temperature readings.
j. Select from temperatures the rows for 'Morning' and 'Evening' temperature
readings.
k. Select from temperatures the columns of temperature readings
for 'Amanda' and 'Maxine'.
l. Select from temperatures the elements for 'Amanda' and 'Maxine' in
the 'Morning' and 'Afternoon'.
m. Use the describe method to produce temperatures’ descriptive statistics.
n. Transpose temperatures.
o. Sort temperatures so that its column names are in alphabetical order.2


Question 2
Using the titanic.csv dataset, write a program to explore and mine the following information:
a) How many passengers were in the titanic?
b) How many male and female passengers were in the titanic?
c) What was the average age of all passengers?
d) How many passengers under 21 years of age?
e) How many survived and how many did not? How many males and how many females?
f) What was the youngest age that survived, and the oldest age? What were their names.
g) Display the name of all passengers that survived.


'''
import numpy as np
import pandas as pd
def q1():
  print('Part A')
  # A) Series ==========
  a = pd.Series([7,11,13,17])  # a.
  print(a)
  b = pd.Series([100.0, 100.0, 100.0, 100.0, 100.0])  # b.
  print(b)
  c = pd.Series([1,2,3,4,5,6,7,8,9,10,20,21,22,23,24,25,26,27,28,29])  # c.
  print(c.describe())
  temperature = pd.Series([98.6, 98.9, 100.2, 97.9], index = ['Julie', 'Charlie', 'Sam', 'Andrea'])  # d.
  print(temperature)
  dict = {'Julie' : 98.6, 'Charlie' : 98.9, 'Sam' : 100.2, 'Andrea' : 97.9}  # e.
  series = pd.Series(dict)
  print(series)

  # B) Dataframes ==========
  print('Part B')  # f.
  dat = {
    'Maxine' : [98.6, 99.1, 98.5],
    'James' : [100.1, 98.2, 88.1],
    'Amanda' : [88.2, 76.2, 101.2]
  }
  temperatures = pd.DataFrame(dat)
  print(temperatures)
  temps = {  # g.
    'Maxine' : [98.6, 99.1, 98.5],
    'James' : [100.1, 98.2, 88.1],
    'Amanda' : [88.2, 76.2, 101.2],
  }
  temperatures = pd.DataFrame(temps, index = ['Morning', 'Afternoon', 'Evening'])
  #temperatures = pd.DataFrame(dat2, index = ['A', 'B', 'C'])
  #print(temperatures)
  print(temperatures)
  print(temperatures.loc[:, ['Maxine']]) # h.
  print(temperatures.loc[['Morning'], :])  # i.
  print(temperatures.loc[['Morning', 'Evening'], :])  # j.
  print(temperatures.loc[:, ['Amanda', 'Maxine']])  # k.
  print(temperatures.loc[['Morning', 'Afternoon'],['Amanda', 'Maxine']])  # l.
  print(temperatures.describe())  # m.
  print(temperatures.transpose())  # n.
  print(temperatures.transpose().sort_index())  # o.

def q2():
  print('Question 2')
  filename = "titanic.csv"
  df = pd.read_csv(filename) # This creates a dataframe from the csv
  z = df.Name.describe()
  print(df.dtypes) # part a
  print(z)
  print(df.sex.value_counts()) #part b
  print(df.mean()) #part c
  print(df[df.age < 21]) #part d
  survived = df.loc[df['survived'] == 'yes']
  died = df.loc[df['survived'] == 'no']
  males_survived = survived.loc[survived['sex'] == 'male']
  males_died = died.loc[died['sex'] == 'male']
  females_survived = survived.loc[survived['sex'] == 'female']
  females_died = died.loc[died['sex'] == 'female']
  # part e
  print("Total survived: ", len(survived))
  print("Total died", len(died))
  print("Total males survived: ", len(males_survived))
  print("Total males died: ", len(males_died))
  print("Total females survived: ", len(females_survived))
  print("Total females died: ", len(females_died))
  y = df.describe()
  #print(y)
  print("The name and age of the oldest that survived: ", '\n', df.sort_values('age', ascending=False).head(1)) # part f
  print('The age of the youngest survivor', survived.loc[1:, ['age']].min())
  print('The name of the youngest survivor', survived.loc[survived['age'] == float(survived.loc[1:, ['age']].min()), ['Name']])
  # part g
  names_survived = survived.loc[1:,['Name']]
  pd.set_option('display.max_rows', None)
  print(names_survived)
q1()
q2()