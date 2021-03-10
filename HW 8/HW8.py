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

# Question 1
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
new_x = x.reshape(3,5)
print(new_x) # Reshapes array into 3 x 5 array

print("a): ", new_x[1,:]) # a) Prints the second row
print("b): ", new_x[:3,3]) # b) Prints column 4
print("c): ", new_x[:1], x[1:2]) # c) Selects rows 0 & 1
print("d): ", "\n", new_x[:, [1,2,3,4]]) # d) Selects columns 2-4
print("e): ", new_x[0,4]) # e) Element at row 1 column 4
print("f): ", new_x[[1,2],:][:, [0,2,4]]) # f Rows 1 & 2 with Columns 0, 2, & 4
