item = input("what item would you like to buy? ")
price = float(input("what is the price of the item? "))
quantity = int(input("how many would you like to buy? "))
total = price * quantity
print(f"you have purchased {quantity} {item}(s) for a total of ${total:.2f}.")