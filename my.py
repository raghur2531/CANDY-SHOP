from func import quantity_added,quantity_remove,quantity_price,owner_use,customer_use,remove_item,display
Quantity = {'Choc':255, 'Ven': 150, 'Orange': 800,'Straw': 100}
Price = {'Choc': 20, 'Ven': 15, 'Orange': 5, 'Straw': 12}
flag=True
while flag:
  print("Candy Shop")
  print("1.For Owner Use")
  print("2.For Customer Purpose")
  print("3.Display Item")
  print("4.Exit")
  choice=int(input("Enter a choice: "))
  if choice == 1:
    print(owner_use())
  elif choice == 2:
    print(customer_use())
  elif choice == 3:
    print(display(Quantity))
  elif choice ==4: 
    print("Exited")
    flag=False
  else:
    print("Enter valid Choice")
