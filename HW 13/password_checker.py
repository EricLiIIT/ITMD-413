"""
Author: Eric Li
A20419312
ITMD 413
HW 13 - Password Checking with Recursive Functions

This program uses recursion to test if a user-input password contains at least one digit.
"""

def does_password_pass_check(passwd, length):
  try:
    if passwd[length].isdigit():
      valid = True
      return valid
    else:
      length = length + 1
      return does_password_pass_check(passwd, length)
  except IndexError:
    print("Invalid password. Try again.")

def main():
  length = 0
  passwd = input("Enter a password: ")
  print("Does your password contain a number: ", does_password_pass_check(passwd, length))
main()
