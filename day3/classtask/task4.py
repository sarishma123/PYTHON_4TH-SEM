
# -----------------------------------------------
# QUESTION 4: Basic Inventory System
# -----------------------------------------------

print("\n" + "=" * 40)
print("QUESTION 4: Inventory System")
print("=" * 40)

inventory = {}  # our inventory dictionary

def add_item():
    name = input("Enter item name: ")
    qty  = int(input("Enter quantity: "))
    if name in inventory:
        print(f"'{name}' already exists! Use Update instead.")
    else:
        inventory[name] = qty
        print(f"'{name}' added with quantity {qty}.")

def update_item():
    name = input("Enter item name to update: ")
    if name in inventory:
        qty = int(input("Enter new quantity: "))
        inventory[name] = qty
        print(f"'{name}' updated to quantity {qty}.")
    else:
        print(f"'{name}' not found in inventory.")

def remove_item():
    name = input("Enter item name to remove: ")
    if name in inventory:
        del inventory[name]
        print(f"'{name}' removed from inventory.")
    else:
        print(f"'{name}' not found in inventory.")

def display_items():
    if inventory:
        print("\n--- Inventory ---")
        for item, qty in inventory.items():
            print(f"  {item}: {qty}")
        print("-----------------")
    else:
        print("Inventory is empty!")

# Main menu loop
while True:
    print("\nOptions: 1-Add  2-Update  3-Remove  4-Display  5-Quit")
    choice = input("Choose (1-5): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        update_item()
    elif choice == "3":
        remove_item()
    elif choice == "4":
        display_items()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1-5.")