item1_name = input("Enter name of item 1: ")
item1_price = float(input("Enter price of item 1: "))

item2_name = input("Enter name of item 2: ")
item2_price = float(input("Enter price of item 2: "))

item3_name = input("Enter name of item 3: ")
item3_price = float(input("Enter price of item 3: "))

# Calculate total
total = item1_price + item2_price + item3_price

# Print formatted receipt
print("\n------ Shopping Receipt ------")
print(f"{item1_name:<20} ${item1_price:>8.2f}")
print(f"{item2_name:<20} ${item2_price:>8.2f}")
print(f"{item3_name:<20} ${item3_price:>8.2f}")
print("-" * 32)

print(f"{'Total':<20} ${total:>8.2f}")