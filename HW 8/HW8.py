'''
Author: Eric Li
A20419312
ITMD 413
Homework 8

(INDEXING AND SLICING ARRAYS) Create an array containing the values 1–15, reshape it
into a 3-by-5 array, then use indexing and slicing techniques to perform each of the following
operations:
a) Select row 2.
b) Select column 4.
c) Select rows 0 and 1.
d) Select columns 2–4.
e) Select the element that is in row 1 and column 4.
f) Select all elements from rows 1 and 2 that are in columns 0, 2 and 4.

'''
import numpy as np

# Question 1
x = np.array([[1, 2, 3, 4, 5],
              [6, 7, 8, 9, 10],
              [11, 12, 13, 14, 15]])
print(x)
