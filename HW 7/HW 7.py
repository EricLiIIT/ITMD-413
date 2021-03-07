'''
Name: Eric Li
ID: A20419312
Homework 7 - Strings and Regular Expressions

This program formats various expressions to demonstrate regular expressions. 

Question 1: Using any text editor, manually create a file that contains four 
or five lines with the following format: 
Username:Firstname:Lastname:Telephone number

Write a program that will convert such lines to a Lightweight Directory Access 
Protocol (LDAP) record format as shown below:
dn: uid=Username, dc=example, dc=com
cn: Firstname Lastname
sn: Lastname
telephoneNumber: Telephone number

Question 2
In some web forms, users must enter a phone number, and some of these aggravate 
users by accepting only a specific format. You have been hired to write a 
program that reads U.S. phone numbers with the three-digit area and seven-digit 
local codes accepted as ten digits, or separated into blocks using hyphens or
spaces, and with the area code optionally enclosed in parentheses. For example, 
all of these are valid: 555-123-1234, (555) 1234567, (555) 123 1234, and 
5551234567. Read the phone numbers from user input and for each one echo the 
number in the form “(999) 999 9999” or report an error for any that are 
invalid, or that don’t have exactly ten digits.
'''
import re 

def q1(): 
    # For question 1
    file = open(r"Z:\ITMD 413 Open Source Programming (Python)\ITMD-413\HW 7\user_list.txt")
    
    for i in file:
        i = i.split(':')
        # Code below takes position of each piece of data
        username = i[0] 
        first_name = i[1]
        last_name = i[2]
        phone_number = i[3]
    
        print(f" dn: uid = {username} dc = gmail, dc = com \n",
        f"cn: {first_name} {last_name} \n",
        f"sn: {last_name} \n", 
        f"Telephone number: {phone_number}") # Use of f-string formatting

def q2():
    # For quesion 2
    phone_number_input = input("Enter phone number: ")
    pattern1 = r'[0-9]+' # This pattern takes only 1 or more numbers
    
    # Go thru list finding numbers --  returns list of strings
    match = re.findall(pattern1, phone_number_input) 
    delimiter = '' # Closes gaps between strings
    fn = delimiter.join(match) # Creates singluar phone number string
    if len(fn) != 10:
        print("Error: Enter correct quantity of digits")
    else:
        print(f"Formatted phone number: ({fn[0:3]}) {fn[3:6]} {fn[6:11]}")

#q1()
q2()