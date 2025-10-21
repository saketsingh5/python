chai_price = int(input("input the chai price to get type of chai"))

if chai_price < 100:
    print(f"Type of chai is in this price {chai_price}: without Ginger")
elif  chai_price > 100: 
    print(f"Type of chai is in this price {chai_price}:  Ginger")
else: 
    print(f"Type of chai is in this price {chai_price}:  cutting chai")



match chai_price:
    case chai_price if chai_price < 100:
     print(f"Type of chai is in this price {chai_price}: without Ginger")
    case chai_price if chai_price > 100:
     print(f"Type of chai is in this price {chai_price}:  Ginger")
    case _:
      print(f"Type of chai is in this price {chai_price}:  cutting chai")