from restaurant import *
from grocery_store import *

def main():
  restaurant1 = Restaurant("Bob's Burgers", "1111 North Main Street", "Open", 0.12, 223, 250, 22, 12)
  restaurant1.tostring()
  print("\n")
  store1 = Grocery_Store("Meg's Market", "2212 West Jackson Ave", "Closed", 0.10, 523, "Restaurant")
  store1.tostring()

  restaurant1.seat_patrons()
  restaurant1.serve_patrons()
  restaurant1.checkout_patrons()
  print("Price per person: $", restaurant1.get_ppp())

  store1.sell_item()
  print("Store type: ", store1.get_store_type())
main()