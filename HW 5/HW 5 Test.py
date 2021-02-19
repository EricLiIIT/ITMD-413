'''
Name: Eric Li
ID: A20419312
Homework 5 - File I/O, and Creating graph using matplotlib package

This program will create a pie chart reflecting the percentage of employees in 
each department within a company and both a line and bar graph of the company's 
profit over the past 10 years. Data will be supplied through specified text 
files. 

'''
# This program displays a simple line graph.
import matplotlib.pyplot as plt
import os

def main():
    f1 = "employee_count_by_department.txt" # Save file as f1
    f2 = "last_ten_year_net_profit.txt" # Save file as f2
    
    if os.path.isfile(f1):
        f1r = open(f1, "r") # Opens file in read mode
        r1 = f1r.readline() # Reads content of file line by line
        
        f1L = [] # List for department quanitites
        dept = [] # List for department names
        while r1 != "": # Reads each line until the next one is empty
            data = r1.split() # Puts all elements into a list, including comma
            label = data[0] # Gets element at location 0 (department name)
            qty = eval(data[2]) # Gets element at location 2 (quantity)
            f1L.append(qty) # Appends to quantity list
            dept.append(label) # Appends to dept name list
            r1 = f1r.readline() # Reads next line?
            
        plt.pie(f1L, labels=dept, autopct='%1.1f%%') # Actually creates pie chart
        plt.title("Quantities of Employees per Department ")
        plt.show() # This shows the chart; though unnecessary in Spyder
        
        f1r.close()
        
    else:
        print("File does not exist in the directory.")
    
    
    if os.path.isfile(f2):
        f2r = open(f2, "r")
        r2 = f2r.readline()
        
        yearList = []
        profitList = []
        
        while r2 != "":
            data = r2.split()
            year = data[0]
            profit = data[2]
            profitList.append(profit)
            yearList.append(year)
            r2 = f2r.readline()
        
        # Creates Line Graph
        plt.plot(yearList, profitList) # Defines axes
        plt.title("Profit per Year (USD)") # Title
        plt.xlabel("Year") # Axis label
        plt.ylabel("Profit (USD)") # Axis label
        plt.grid(True) # Adds grid
        plt.show()
        
        # Creates Bar Graph
        plt.bar(yearList, profitList)
        plt.title("Profit per Year (USD)")
        plt.xlabel("Year")
        plt.ylabel("Profit (USD)")
        plt.show()
    
    else:
       print("File does not exist in the directory.")
            
main()