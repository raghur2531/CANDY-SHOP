Quantity = {'Choc':255, 'Ven': 150, 'Orange': 800,'Straw': 100}
Price = {'Choc': 20, 'Ven': 15, 'Orange': 5, 'Straw': 12}
def add_item(item,quantity,):
  if item not in Quantity:
    quantity =input(f"Enter the quantity of {item}")
    Quantity[item] = quantity
    print(f"{item} added to the shop.")
  else:
    print(f"{item} already exists in the shop.")
def quantity_added(item):
  if item in Quantity:
    add=int(input("Enter the Quantity to add:"))
    Quantity[item] += add
    print(f"{add} {item} added to the shop.")
  else:
    print(f"{item} is not available in the shop.")
def quantity_remove(item):
  if item in Quantity:
    remove=int(input("Enter the Quantity to remove:"))
    Quantity[item] -= remove
    print(f"{remove} {item} removed in the shop.")
  else:
    print(f"{item} is not available in the shop.")
def quantity_price(item):
    if item in Quantity:
      quantity = int(input("Enter the Quantity: "))
      if item in Price:
        price = Price[item]
        total_price = quantity * price
        print(f"Total price for {quantity} {item} is: {total_price}")
      else:
        flag = False
    else:
      print(f"{item} is not available in the shop.")
      flag = False
def display(Quantity):
  print("Items in the shop:")
  for item,quantity in Quantity.items():
    print(item, quantity, Price[item])
def remove_item(item):
  if item in Quantity:
    del Quantity[item]
    print(f"{item} removed from the shop.")
  else:
    print(f"{item} is not available in the shop.")
def owner_use():
  print("1.Adding Quantity")
  print("2.Removing Quantity")
  print("3.Add item")
  print("4.Quantity present")
  print("5.Remove item")
  print("6. Exit")
  Choice=int(input("Enter a choice: "))
  if Choice == 1:
    item = input("Enter the item name: ")
    print(quantity_added(item))
  elif Choice == 2:
    item = input("Enter the item name: ")
    print(quantity_remove(item))
  elif Choice ==3:
    item =input("Enter the item name:")
    add_item(item,quantity)
  elif Choice ==4:
    print(Quantity)
  elif Choice ==5:
    item =input("Enter the item name:")
    remove_item(item)
  elif Choice ==6:
    print("Exited")
    flag=False
  else:
    print("Enter valid Choice")
  return
def customer_use():
  print("1.Price Detail")
  print("2.Total Price")
  print("3.Exit")
  Choice=int(input("Enter a choice: "))
  if Choice == 1:
    print(Price)
  elif Choice == 2:
    item=input("Enter the item name:")
    print(quantity_price(item))
  elif Choice == 3:
    print("Exited")
    flag=False
  else:
    print("Enter valid Choice")
  return()
