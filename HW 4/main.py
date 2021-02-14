'''
Name: Eric Li
ID: A20419312
Homework 4 - Lists/Arrays

This is the main method that runs the functions from the other program files. 

Question 1:
Write a program called SellItems. The program should allow the user to enter 
any number of item prices and then calculate the total and apply a 7% sales 
tax. The item prices should be stored in a Python list, and a loop should be 
used to get the input and calculate the total. The output should include a list 
of item prices, the subtotal of the prices, the tax amount, and the final
cost. Display all results in two decimal places. Create at least two functions 
and save the functions into a separate file (the file that you have created in 
hw3). Import the file in your main program.

Question 2:
Multiply two user input matricies.
'''
from SellItems import *
import numpy as np

def main():
    #calc(item())
    # These take in the values for the first matrix

    b = range(3) 
    m1a = []
    m1b = []
    m1c = []
    for a in b:
        i = float(input("Enter number for your first matrix: "))
        m1a.append(i)
    for a in b:
        i = float(input("Enter number for your first matrix: "))
        m1b.append(i)
    for a in b:
        i = float(input("Enter number for your first matrix: "))
        m1c.append(i)
    print("=======================================")
   
    # These take in the values for the first matrix
   
    m2a = []
    m2b = []
    m2c = []
    for a in b:
        i = float(input("Enter number for your second matrix: "))
        m2a.append(i)
    for a in b:
        i = float(input("Enter number for your second matrix: "))
        m2b.append(i)         
    for a in b:
        i = float(input("Enter number for your second matrix: "))
        m2c.append(i)
    # The following two lines create the matricies 
    m1 = np.array([m1a, m1b, m1c]) 
    m2 = np.array([m2a, m2b, m2c])
    matrix = m1 @ m2
    multiplyMatrix(m1, m2)

main()
