'''
Author: Eric Li
A20419312
ITMD 413
HW 10

This program allows for a user to save names and emails to a dictionary
as key value pairs. Changes made to the dictrionary are saved to a file.
Upon starting the program the dictionary is unbound, and on closing it is
rebound.
'''
import pickle
import os

def menu():
  choice = input("""
  Enter:
  1. To find an email address
  2. To add a new name and email address
  3. To change an existing email address
  4. To delete an existing name and email address
  0. To save and stop the program
  """)
  return choice

def find(file_read): # Looks for name and email pair
  name_in = input("Enter name to find email: ")
  if name_in in file_read:
    print(file_read[name_in])
  else:
    print("Does not exist")

def add(file_read): # Adds new key pair
  name = input("Enter new name: ")
  email = input("Enter new email address:")
  file_read[name] = email # Creates key pair
  print("Successfully added", file_read)

def change(file_read): # Updates key pair
  name = input("Enter the name of the person whose email you would like to change: ")
  new_email = input("Enter the new email: ")
  del file_read[name] # Deletes key pair so it will be re-added
  file_read[name] = new_email # "Updates" key pair
  print("Successfully changed email")

def delete(file_read): # Deletes key pair
  name_in = input("Enter the name of the person you would like delete: ")
  del file_read[name_in]
  print("Successfully deleted")

def all(file_read):
  print(file_read) # Prints entire list of names and employees

def delete_all(file_read): # Deletes content of entire file
  del file_read
  print("Successfully deleted all entries")

def main():
  if os.path.getsize("dictionary.txt") == 0: # Checks if file is empty and decides to read or create
    file_read = dict()
  else:
    file_read = pickle.load(open("dictionary.txt", "rb")) # Reads byte stream into Python

  choice = menu()
  while True: # Checks use input choices
    if choice == "1":
      find(file_read)
    elif choice == "2":
      add(file_read)
    elif choice == "3":
      change(file_read)
    elif choice == "4":
      delete(file_read)
    elif choice == "5":
      all(file_read)
    elif choice == "6":
      delete_all(file_read)
    elif choice == "0":
      print("===Saved===")
      break
    else:
      print("Invalid input")
    choice = menu()
  pickle.dump(file_read, open("dictionary.txt", "wb")) # Writes data to file

main()