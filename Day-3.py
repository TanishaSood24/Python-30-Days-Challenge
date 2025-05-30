
inventory = {}

# Add or update items in your stock
def add_item(item, qty):
    if item in inventory:
        inventory[item] += qty
        print(f"Updated! You now have {inventory[item]} {item}(s).")
    else:
        inventory[item] = qty
        print(f"Added {qty} {item}(s) to your inventory.")

# Remove items (like when used or sold)
def remove_item(item, qty):
    if item in inventory and inventory[item] >= qty:
        inventory[item] -= qty
        print(f"{qty} {item}(s) removed. {inventory[item]} remaining.")
        if inventory[item] == 0:
            print(f"Oops! {item} is out of stock now.")
    else:
        print(f"Can't remove {qty} {item}(s). Either not enough in stock or item doesn't exist.")

# Check how much of an item you have
def check_quantity(item):
    return inventory.get(item, 0)

# Let's try it out
add_item("apple", 10)
add_item("banana", 5)
remove_item("apple", 3)
print(f"Banana count: {check_quantity('banana')}")
remove_item("banana", 6)  # More than available - should show an error

