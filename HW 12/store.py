"""
Author: Eric Li
A20419312
ITMD 413
HW 12

This program demonstrates the use implementation of object oriented programming.
"""
from abc import ABC, abstractmethod
import datetime

class Store(ABC):
  # Default constructor
  def __init__(self, name, address, availability, sales_tax):
    self.store_name = name
    self.address = address
    self.availability = availability
    self.sales_tax = sales_tax
    super().__init__(name, address, availability, sales_tax)

  def get_name(self, name):
    self.store_name = name

  def set_name(self, name):
    return(self.store)

  def get_address(self, address):
    self.address = address

  def set_address(self, address):
    return(self.address)

  def get_availability(self, availability):
    self.availability = availability

  def set_availability(self, availability):
    return(self.availability)

  def get_sales_tax(self, sales_tax):
    self.sales_tax = sales_tax

  def set_sales_tax(self, sales_tax):
    return(self.sales_tax)

  @abstractmethod
  def calculate_total_sales_tax(self):
    pass

  @abstractmethod
  def calculate_total_sales(self):
    pass
