from store import *

class Restaurant(Store):
  # Default constructor
  def __init__(self, name, address, availability, sales_tax, total_served, max_occupancy, current_occupancy, ppp): # ppp is price per person
    super().__init__(name, address, availability, sales_tax)
    self.total_served = total_served
    self.max_occupancy = max_occupancy
    self.current_occupancy = current_occupancy
    self.ppp = ppp

  def seat_patrons(self):
    to_be_seated = eval(input("Enter the amount of people to be seated: "))
    self.current_occupancy += to_be_seated

    if to_be_seated <= self.max_occupancy:
      print("Welcome to Bob's Burgers")
      return True
    else:
      print("We are at capacity. We appreciate your patience")
      return False

  def serve_patrons(self):
    to_be_served = eval(input("Enter the amount of people to be served: "))
    self.total_served += to_be_served
    currently_serving = self.current_occupancy + to_be_served
    return currently_serving

  def checkout_patrons(self):
    patrons_leaving = eval(input("Enter the amount of customers leaving: "))
    self.current_occupancy -= patrons_leaving
    return self.current_occupancy

  def set_ppp(self, ppp):
    self.ppp = ppp

  def get_ppp(self):
    return self.ppp

  def tostring(self): # Method to print restaurant attributes
    print(self.store_name)
    print(self.address)
    print(self.availability)
    print(self.sales_tax)
    print(self.total_served)
    print(self.max_occupancy)
    print(self.current_occupancy)
    print(self.ppp)

  def calculate_total_sales_tax(self):
    return self.ppp * self.total_served * self.sales_tax

  def calculate_total_sales(self):
    return self.total_served * self.ppp


