from store import *

class Grocery_Store(Store):
  def __init__(self, name, address, availability, sales_tax, total_revenue, store_type):
    super().__init__(name, address, availability, sales_tax)
    self.total_revenue = total_revenue
    self.store_type = store_type

  def sell_item(self):
    quantity = eval(input("Input quantity of item: "))
    price = eval(input("Enter price of item: "))

    total_revenue = price*quantity
    return total_revenue

  def set_store_type(self, store_type):
    self.store_type = store_type

  def get_store_type(self):
    return self.store_type

  def tostring(self):
    print(self.store_name)
    print(self.address)
    print(self.availability)
    print(self.sales_tax)
    print(self.total_revenue)
    print(self.store_type)