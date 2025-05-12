import re

inventory = [
    {'name': 'bread', 'price': 23.9, 'quantity': 8},
    {'name': 'salt', 'price': 15.3, 'quantity': 15},
    {'name': 'soda 250ml', 'price': 36, 'quantity': 20},
    {'name': 'mint', 'price': 9.5, 'quantity': 66},
    {'name': 'gum', 'price': 1, 'quantity': 150}
]

def validate_text_with_spaces(text):
    return bool(text.strip())

def validate_letters_and_spaces(text):
    # Allows only letters (uppercase and lowercase) and spaces
    return bool(re.fullmatch(r'[a-zA-Z\s]+', text))

def validate_number(message):
    while True:
        try:
            value_str = input(message)
            value = float(value_str)
            if value >= 0:
                return value
            else:
                print("The value must be a positive number")
        except ValueError:
            print("Invalid, Please enter a number")

def validate_quantity(message):
    while True:
        try:
            value_str = input(message)
            value = int(value_str)
            if value >= 0:
                return value
            else:
                print("Invalid, quantity must be a positive integer")
        except ValueError:
            print("Invalid, Please enter an integer")

def add_product():
    """Allows the user to add a new product to the inventory."""
    while True:
        name = input("Enter the product name: ").strip().lower()
        if not validate_letters_and_spaces(name):
            print("The product name cannot contain numbers or special characters.")
            continue

        if name in [item['name'] for item in inventory]:
            print(f"The product {name} already exists. If you want to update the information for {name}, select option 3.")
            return

        price = validate_number("Enter the product price: ")
        quantity = validate_quantity("Enter the quantity of products you want to add to the inventory: ")

        product = {'name': name, 'price': price, 'quantity': quantity}
        inventory.append(product)
        print(f"The product {name} has been successfully added to the inventory.")
        break

def consult_product():
    """Allows the user to search for a product by name and display its details."""
    while True:
        product_name = input("Enter the name of the product you want to search for: ").strip().lower()
        valid = all(character.isalpha() or character == "" for character in product_name)

        if valid and product_name:
            break
        else:
            print("The product name should not contain numbers or special characters.")
    found = False
    for product in inventory:
        if product['name'].lower() == product_name.lower():
            print("\n--- Product Details ---")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Quantity: {product['quantity']}")
            found = True
            break
    if not found:
        print(f"No product found with the name '{product_name}'.")

def update_price():
    """Allows the user to modify the price of an existing product."""
    name_to_update = input("Enter the name of the product you want to update: ").strip().lower()
    exists = False
    for product in inventory:
        if product['name'].lower() == name_to_update:
            try:
                new_price = float(input(f"Enter the new price for '{product['name']}': "))
                if new_price < 0:
                    print("The price cannot be negative.")
                    return
                product['price'] = new_price
                print(f"The price of '{product['name']}' has been updated to ${new_price:.2f}")
                exists = True
            except ValueError:
                print("Invalid input, please enter a valid number for the price.")
            break
    if not exists:
        print(f"No product found with the name '{name_to_update}'.")

def delete_product():
    """Allows the user to delete a product from the inventory."""
    name_to_delete = input("Enter the name of the product you want to delete: ").strip()
    index_to_delete = -1
    for i, product in enumerate(inventory):
        if product['name'].lower() == name_to_delete.lower():
            index_to_delete = i
            break
    if index_to_delete != -1:
        deleted_product = inventory.pop(index_to_delete)
        print(f"The product '{deleted_product['name']}' has been successfully deleted from the inventory.")
    else:
        print(f"No product found with the name '{name_to_delete}'.")

def calculate_total_value():
    """Calculates and displays the total value of the inventory."""
    total_value = 0
    for product in inventory:
        total_value += product['price'] * product['quantity']
    print(f"\nThe total value of the inventory is: ${total_value:.2f}")

def show_inventory():
    """Displays the current inventory in detail."""
    if not inventory:
        print("The inventory is empty.")
        return
    print("\n--- Inventory ---")
    for product in inventory:
        print(f"Name: {product['name']}")
        print(f"Price: ${product['price']:.2f}")
        print(f"Quantity: {product['quantity']}")
        print("-" * 20)

# Main menu to interact with the inventory
while True:
    print("\n--- Menu ---")
    print("1. Add product")
    print("2. Consult product")
    print("3. Update product price")
    print("4. Delete product")
    print("5. Calculate total inventory value")
    print("6. Show complete inventory")
    print("7. Exit")

    option = input("Select an option: ")

    if option == '1':
        add_product()
    elif option == '2':
        consult_product()
    elif option == '3':
        update_price()
    elif option == '4':
        delete_product()
    elif option == '5':
        calculate_total_value()
    elif option == '6':
        show_inventory()
    elif option == '7':
        print("Goodbye")
        break
    else:
        print("Invalid option, please try again.")