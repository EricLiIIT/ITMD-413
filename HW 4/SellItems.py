'''
Name: Eric Li
ID: A20419312
Homework 4 - Lists/Arrays

This program ingests prices input by a user and calculates the sales tax.

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
import numpy as np

def item(): # This method intakes the user input prices
    prices = []
    
    print("Enter zero when you are done entering prices")
    while True: # Loops to continuously accept prices
        p = float(input("Enter price: "))
        if p == 0:
            #print(prices)
            break
        prices.append(p)
    return prices
    
def calc(prices): # This method primarily prints the input & processed information
    subTotal = sum(prices) # Sums prices
    tax = 0.07
    gt = (subTotal * tax) + subTotal # Tallys grand total
    print("Each price entered: ", prices)
    print("The subtotal is: ", '$', subTotal)
    print("The tax of your total is: ", '${:.2f}'.format(tax * subTotal))
    print("The total with sales tax is: ", '${:.2f}'.format(gt))       

def multiplyMatrix(m1, m2):

    matrix = m1 @ m2
    print(matrix)
    
    


