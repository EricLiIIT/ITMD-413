import tkinter as tk
from tkinter import *

root = Tk()
root.title("Change Counter")
root.geometry('500x500')
root.configure(background = "white")

class Coin():
  def __init__(self, main):

    instructions = Label(root, bg="white",text = "Enter coin quantity in respective sections")
    instructions.grid(row = 0, column = 1)
    quantity_label = Label(root, bg="white", text = "Quantity")
    quantity_label.grid(row=1, column = 2)

    dollar_label = Label(root, bg="white", text = "Dollar Coins").grid(row = 2,column = 0)
    dollar = Entry(root)
    dollar.grid(row = 2,column = 1) # .grid() and other functions (.pack(), .place()) on Entry object returns None
    dollar_ct = Label(root, bg="white", text="")
    dollar_ct.grid(row=2, column=2)

    half_dollar_label = Label(root, bg="white", text = "Half Dollar Coins").grid(row = 3,column = 0)
    half_dollar = Entry(root)
    half_dollar.grid(row = 3,column = 1)
    half_dollar_ct = Label(root, bg="white", text="")
    half_dollar_ct.grid(row=3, column=2)

    quarter_label = Label(root, bg="white", text = "Quarters").grid(row = 4,column = 0)
    quarter = Entry(root)
    quarter.grid(row = 4,column = 1)
    quarter_ct = Label(root, bg="white", text="")
    quarter_ct.grid(row=4, column=2)

    dime_label = Label(root, bg="white", text = "Dimes").grid(row = 5,column = 0)
    dime = Entry(root)
    dime.grid(row = 5,column = 1)
    dime_ct = Label(root, bg="white", text="")
    dime_ct.grid(row=5, column=2)

    nickel_label = Label(root, bg="white", text = "Nickels").grid(row = 6,column = 0)
    nickel = Entry(root)
    nickel.grid(row = 6,column = 1)
    nickel_ct = Label(root, bg="white", text="")
    nickel_ct.grid(row=6, column=2)

    penny_label = Label(root, bg="white", text = "Pennies").grid(row = 7,column = 0)
    penny = Entry(root)
    penny.grid(row = 7,column = 1)
    penny_ct = Label(root, bg="white", text="")
    penny_ct.grid(row=7, column=2)

    self.btn = tk.Button(main, text="Submit", command=self.print_quantity).grid(row=8,column=1)
    self.btn2 = tk.Button(main, text="Calculate", command=self.calculate).grid(row=8,column=2)

  def print_quantity(self, dollar, dollar_ct, half_dollar, half_dollar_ct, quarter, quarter_ct, dime, dime_ct, nickel, nickel_ct, penny, penny_ct):
    self.dollar_ct.config(text=self.dollar.get())
    self.half_dollar_ct.config(text=self.half_dollar.get())
    self.quarter_ct.config(text=self.quarter.get())
    self.ime_ct.config(text=self.dime.get())
    self.nickel_ct.config(text=self.nickel.get())
    self.penny_ct.config(text=self.penny.get())

  def calculate(self, dollar, half_dollar, quarter, dime, nickel, penny):
    total = float(self.dollar.get()) * 1
    total += float(self.half_dollar.get()) * 0.5
    total += float(self.quarter.get()) * 0.25
    total += float(self.dime.get()) * 0.1
    total += float(self.nickel.get()) * 0.05
    total += float(self.penny.get()) * 0.01
    print('{:.2f}'.format(total))

coin1 = Coin(root)
root.mainloop()
#messagebox.showinfo("Submitted", "Thank You!")

