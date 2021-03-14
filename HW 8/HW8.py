'''
Author: Eric Li
A20419312
ITMD 413
Homework 8

Question 1
(INDEXING AND SLICING ARRAYS) Create an array containing the values 1–15, reshape it
into a 3-by-5 array, then use indexing and slicing techniques to perform each of the following
operations:
a) Select row 2.
b) Select column 4.
c) Select rows 0 and 1.
d) Select columns 2–4.
e) Select the element that is in row 1 and column 4.
f) Select all elements from rows 1 and 2 that are in columns 0, 2 and 4.

Question 2

For this question, please use NumPy Python library. Make sure you have installed NumPy,
Pandas, SciPy, and Matplotlib Python libraries. Use command pip (for Windows) or pip3 (for
MacOS).
Write a program to load a given dataset called Student_Grades.csv into a NumPy array. Then
determine the following items:
a) Display all data on screen.
b) Determine how many students were in the dataset?
c) Display the number of rows and columns of your numpy array.
d) Display the array data types.
e) Display the following Descriptive Statistics of students’ overall percentage scores:
  a. Min score
  b. Max score
  c. Mean value
  d. Median
  e. Mode
  f. Standard Deviation
  g. 25% and 75% percentile
  f) Determine how many students achieved an A grade, B, C, D and F grades.
  g) Create a pie chart based on the above grade achievements (option f)
'''
import numpy as np
from numpy import genfromtxt
from scipy import stats
import matplotlib.pyplot as plt
import sys

# Question 1
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
new_x = x.reshape(3,5)
print(new_x) # Reshapes array into 3 x 5 array
print("a): ", new_x[2,:]) # a) Prints the second row
print("b): ", new_x[:4,4]) # b) Prints column 4
print("c): ", "\n", new_x[:2]) # c) Selects rows 0 & 1
print("d): ", "\n", new_x[:, [2,3,4]]) # d) Selects columns 2-4
print("e): ", new_x[1,4]) # e) Element at row 1 column 4
print("f): ", "\n", new_x[1:3, [0,2,4]]) # f Rows 1 & 2 with Columns 0, 2, & 4

# Question 2
grade_array = genfromtxt('Student_Grades.csv', delimiter = ',', skip_header = 1)
np.set_printoptions(threshold=sys.maxsize) # Shows all values in the array
#print(grade_array.size)
#print("a)", grade_array)
grade_array = grade_array.reshape(33,32) # 33 rows, 32 columns
#print(grade_array[:, 0])
print(type(grade_array))
print("a)", grade_array)
qty_rows, qty_cols = grade_array.shape
print("b)", "There are ", qty_rows, "students.")
print("c)", "There are",qty_rows, "rows and", qty_cols, "columns")
print("d)", grade_array.dtype)

# Methods to calculate percentages:
print("e)","\n")
percentage_array = grade_array[:33,31] # Gets the last column and assigns it to percentage_array
percentage_array = percentage_array.flatten()
min_score = np.amin(percentage_array)
print("Minimum score: ", min_score)
max_score = np.max(percentage_array)
print("Max score: ", max_score)
average = np.average(percentage_array)
print("Average: ", average)
median = np.median(percentage_array)
print("Median: ", median)
mode = stats.mode(percentage_array)
print("Mode: ", mode[0]) # Removing [0] gets more info
std_dev = np.std(percentage_array)
print("This is the standard deviation: ", std_dev)
distrib25 = np.percentile(percentage_array, 25)
print("25th Percentile: ", distrib25)
distrib75 = np.percentile(percentage_array, 75)
print("75th Percentile: ", distrib75)

print("A: ", np.count_nonzero(percentage_array>90)) # Calculates the amount of A's in the class
print("B: ", np.count_nonzero((percentage_array>79)&(percentage_array<90), axis = 0)) # Calculates the amount of B's in the class
print("C: ", np.count_nonzero((percentage_array>69)&(percentage_array<80), axis = 0)) # Calculates the amount of C's in the class
print("D: ", np.count_nonzero((percentage_array>59)&(percentage_array<70), axis = 0)) # Calculates the amount of D's in the class
print("F: ", np.count_nonzero(percentage_array<60, axis = 0)) # Calculates the amount of f's in the class

labels = "A", "B", "C", "D", "F"
sizes = [21, 8, 1, 1, 2]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.show()

#WARNING: You are using pip version 20.2.3; however, version 21.0.1 is available.
#You should consider upgrading via the 'c:\python 3.8.2\python38\python.exe -m pip install --upgrade pip' command.