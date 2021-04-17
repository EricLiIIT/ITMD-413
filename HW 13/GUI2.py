import tkinter as tk
from tkinter import *

class Coin():
  def __init__(self, dol, hdol, quart, dime, nick, pen):
    self.dol = dol
    self.hdol = hdol
    self.quart = quart
    self.dime = dime
    self.nick = nick
    self.pen = pen

  #Setters and Getters for coin types
  def calc_dol(self):
    return self.dol

  def calc_hdol(self):
    return self.hdol * .5

  def calc_quart(self):
    return self.quart * .25

  def calc_dime(self):
    return self.dime * 0.10

  def calc_nick(self):
    return self.nick * .05

  def calc_pen(self):
    return self.pen * .01

  def set_dol(self, dol):
    self.dol = dol
  def get_dol(self):
    return dol

  def set_hdol(self, hdol):
    self.hdol = hdol
  def get_hdol(self):
    return hdol

  def set_quart(self, quart):
    self.quart = quart
  def get_quart(self):
    return quart

  def set_dime(self, dime):
    self.dime = dime
  def get_dime(self):
    return dime

  def set_nick(self, nick):
    self.nick = nick
  def get_nick(self):
    return nick

  def set_pen(self, pen):
    self.pen = pen
  def get_pen(self):
    return pen

def calculate(root, dol_in, hdol_in, quart_in, dime_in, nick_in, pen_in):
  try:
    dol_in = int(dol_in.get())
    hdol_in = int(hdol_in.get())
    quart_in = int(quart_in.get())
    dime_in = int(dime_in.get())
    nick_in = int(nick_in.get())
    pen_in = int(pen_in.get())

    coin1 = Coin(dol_in, hdol_in, quart_in, dime_in, nick_in, pen_in)
    dollars = float(coin1.calc_dol())
    half_dollars = float(coin1.calc_hdol())
    quarters = float(coin1.calc_quart())
    dimes = float(coin1.calc_dime())
    nickels = float(coin1.calc_nick())
    pennies = float(coin1.calc_pen())
    total = dollars + half_dollars + quarters + dimes + nickels + pennies
    formatted_total = "{:.2f}".format(total)
    Label(root, text=formatted_total).grid(row=7, column=6)

  except ValueError:
    print("Invalid Input. Try again.")

def main():
  try:
    root = Tk()
    root.title("Change Counter")
    root.geometry('500x500')
    #root.configure(background = "white")

    instructions = Label(root, text = "Enter coin quantity in respective sections. Enter 0 in sections where you have none of that coin.", wraplength=300).grid(row=0, column=0)

    dol_label = Label(root, text = "Dollar Coins")
    dol_label.grid(row=1,column=0) # .grid() and other functions (.pack(), .place()) on Entry object returns None
    dol_in = Entry(root)
    dol_in.grid(row=1, column=6)

    hdol_label = Label(root, text = "Half - Dollar Coins")
    hdol_label.grid(row=2,column=0)
    hdol_in = Entry(root)
    hdol_in.grid(row=2, column=6)

    quart_label = Label(root, text = "Quarters")
    quart_label.grid(row=3,column=0)
    quart_in = Entry(root)
    quart_in.grid(row=3, column=6)

    dime_label = Label(root, text = "Dimes")
    dime_label.grid(row=4,column=0)
    dime_in = Entry(root)
    dime_in.grid(row=4, column=6)

    nick_label = Label(root, text = "Nickels")
    nick_label.grid(row=5,column=0)
    nick_in = Entry(root)
    nick_in.grid(row=5, column=6)

    pen_label = Label(root, text = "Pennies")
    pen_label.grid(row=6,column=0)
    pen_in = Entry(root)
    pen_in.grid(row=6, column=6)

    Label(root, text = "Total: $").grid(row=7, column=5)
    #total = Entry(root).grid(row=7, column=6)

    btn = Button(root, text="Calculate", command = lambda: calculate(root, dol_in, hdol_in, quart_in, dime_in, nick_in, pen_in))
    btn.grid(row=8, column=6)

    root.mainloop()
  except ValueError:
    print("Invalid Input. Try again.")

main()