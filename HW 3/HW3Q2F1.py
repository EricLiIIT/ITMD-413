"""
Name: Eric Li
ID: A20419312
Homework 3 - Functions and Functions on a Separate File

This program calculates the retail price based on the input from the calculate
function's input. 

Question 2
Given a complete program below, rewrite the program using functions. Create at 
least two functions. Put your function into a separate file and import the 
file when you write your main program. Save your functions file using the file 
you have created in Question #1.
"""
import HW3Q2F2 as f4
def retail():
    # This program calculates retail prices.
    mark_up = 2.5 # The markup percentage
    another = 'y' # Variable to control the loop.
    
    # Process one or more items.
    while another == 'y' or another == 'Y':
        # Get the item's wholesale cost.
        a = f4.calculate()
        # Validate the wholesale cost.
        
        while a < 0:
            print('ERROR: the cost cannot be negative.')
            a = float(input('Enter the correct wholesale cost:'))
        # Calculate the retail price.
        retail = a * mark_up
        # Display the retail price.
        print('Retail price: $', format(retail, ',.2f'))
        # Do this again?
        another = input('Do you have another item? (Enter y for yes): ')
