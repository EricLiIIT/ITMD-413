'''
Name: Eric Li
ID: A20419312
Homework 2 - Simple I/O, Control Structures, and Looping Concepts

This program determines how many years it takes for the Mexican population to exceed the US population, 
as well as printing out the population for each year. 
The second half of the program follows the troubleshooting chart for a diesel engine. It takes in user 
input and guides them through which steps to take. 

Question 1
The current population of the United States is about 328.2 million and that the population
decreases 0.53 percent annually. The current population of Mexico is 127.6 million and
that the population increases 1.06 percent annually. Assume the population percentages
for both countries remain the same, write a program that displays the populations for the
two countries every year until the population of Mexico exceeds that of the United States,
and display the number of years it took. 

Question 2
Observe the Troubleshooting Chart for Diesel Engine below. Write a program based on the given
chart. Make sure your program validates the input data. For example, value 50x is invalid, it
should be 50.
'''

# Question 1
usPop = 328200000 
mexPop = 127600000

usMult = 0.0053
mexMult = 0.0106

yearct = 0

while mexPop < usPop:
    usPop = usPop - (usPop * usMult)
    mexPop = mexPop + (mexPop * mexMult)
    print("US Population: ", "{:.0f}".format(usPop), "\n", "Mexican Population: ", "{:.0f}".format(mexPop))
    yearct += 1
    print(yearct)

    
print("It will take",yearct, "years for the Mexican population to exceed the US population")
print("The US Population will be", "{:.0f}".format(usPop), "in", yearct, "years")
print("The Mexican Population will be", "{:.0f}".format(mexPop), "in", yearct, "years")

# Question 2
def question2():
    def Red():
        try:
            meter = float(input("Enter meter value"))
            if meter < 50:
                print("Check main line for test pressure")
                pressure = input("What is the pressure level? (Normal, High, Low)")
                if pressure == "Normal" :
                    print("Refer to motor service manual")
                elif pressure == "High" or pressure == "Low": 
                    print("Refer to main line manual")
                #else:
                    #print("Please enter valid input")
            elif meter >= 50: 
                flow = input("Measure and enter flow velocity at inlet 2-B (Normal, High, Low): ")
                if flow == "Normal":
                    print("Refer to inlet service manual")
                elif flow == "High" or flow == "Low": 
                    print("Return unit for factory service")
                #else:
                    #print("Please enter valid status")
            #else:
                #print("Please enter valid number")
        except:
            print("Error: enter valid input")
    
    def light():
        try: 
            statusLight = input("What color is the engine light? (Green, Red, Amber)")
            if statusLight == "Green":
                print("Do restart procedure")
            elif statusLight == "Red":
                print("Shut off all input lines anc check meter #3")
                Red()
            elif statusLight == "Amber":
                print("Check fuel line service routine")
                Amber()
            #else:
                #print("Please enter a valid color")
        except:
            print("Error: enter valid input")
    light()
    
    def Amber():
        print("Check fuel line service routine")
            
question2()
