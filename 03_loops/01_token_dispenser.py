for token in range(1,11):
    print(f"serving chai to token {token}")

orders = ["saket", "singh", "new"]
bills = [20,40,30]

for name in orders: print(f"serving chai to token {name}")

# enumerate
for index, item in enumerate(orders):
    print(f"{index}, {name}")


# zip
for name, amount in zip(orders, bills):
     print(f"{name} bill {amount}")


# Walrus operator
value = 13 
if(remainder := value % 5 ):
    print(f"remainder is {remainder}")     