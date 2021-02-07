"""
Name: Eric Li
ID: A20419312
Homework 3 - Functions and Functions on a Separate File

This function converts degrees to radians. 

Question 1
In Python, subprograms are called functions. Each function in a program should 
do one and only one subtask. Data get passed back and forth between the “main” 
section of the program and various functions. The main part may pass data to a 
function, receive new data from a function, or both. Data received from a 
function could in turn be passed on to another function. You can imagine data 
flowing along the connecting lines in the structure chart. That’s how we 
“empower these subprograms to work together.” Create functions for converting 
between radians and degrees. Since most of the trigonometric functions require 
that the angle is expressed in radians, we will create our own functions in 
order to convert between radians and degrees. It is quite easy to convert from 
radians to degrees or from degrees to radians. Create two functions that 
convert from radians to degrees (r2d(x)) and from degrees to radians (d2r(x)) 
respectively. Save your functions into a separate Python file and import the 
file when you write your main program. Test the functions thoroughly to make 
sure that they work as expected. 

"""
import math

def degToRad():
    d = float(input("Enter degrees: "))
    r = d * (math.pi/180)
    print(r)

