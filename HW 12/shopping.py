from restaurant import *
from grocery_store import *

def main(): # Creates instances of restaurant and grocery_store classes

  restaurant1 = Restaurant("Bob's Burgers", "1111 North Main Street", "Open", 0.12, 223, 250, 22, 12)
  restaurant1.tostring()
  print("\n")
  restaurant1.seat_patrons()
  restaurant1.serve_patrons()
  restaurant1.checkout_patrons()
  print("Price per person: $", restaurant1.get_ppp())
  print("Sales tax: ", restaurant1.calculate_total_sales_tax())
  print("Total Revenue: ", restaurant1.calculate_total_sales() + restaurant1.calculate_total_sales_tax())

  store1 = Grocery_Store("Meg's Market", "2212 West Jackson Ave", "Closed", 0.10, 0, "Restaurant")
  print("Store type: ", store1.get_store_type())
  store1.tostring()
  store1.sell_item()
  print("Sales Tax: ", store1.calculate_total_sales_tax())
  print("Total Revenue: ", store1.calculate_total_sales() + store1.calculate_total_sales_tax())

main()