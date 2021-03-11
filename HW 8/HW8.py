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

'''
import numpy as np
from numpy import genfromtxt
import sys

# Question 1
'''
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
new_x = x.reshape(3,5)
print(new_x) # Reshapes array into 3 x 5 array

print("a): ", new_x[1,:]) # a) Prints the second row
print("b): ", new_x[:3,3]) # b) Prints column 4
print("c): ", new_x[:1], x[1:2]) # c) Selects rows 0 & 1
print("d): ", "\n", new_x[:, [1,2,3,4]]) # d) Selects columns 2-4
print("e): ", new_x[0,4]) # e) Element at row 1 column 4
print("f): ", new_x[[1,2],:][:, [0,2,4]]) # f Rows 1 & 2 with Columns 0, 2, & 4
'''

# Question 2
'''
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

grade_array = genfromtxt('Student_Grades.csv', delimiter = ',', skip_header = 1)
np.set_printoptions(threshold=sys.maxsize)
print(grade_array.size)
#print("a)", grade_array)
grade_array = grade_array.reshape(33,32) # 33 rows, 32 columns
#print(grade_array[:, 0])

#print(type(grade_array))
#print("a)", grade_array)
qty_rows, qty_cols = grade_array.shape
#print("b)", "There are ", qty_rows, "students.")
#print("c)", "There are",qty_rows, "rows and", qty_cols, "columns")
#print("d)", grade_array.dtype)

# Methods to calculate percentages:
percentage_array0 = np.divide(grade_array[:, 0], 15)
percentage_array0 = np.multiply(percentage_array0, 100)
print(percentage_array0)
