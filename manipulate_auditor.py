import json
import os


def load_inventory():
    #Check whether inventory.json exists
    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        #Open the JSON file for reading
        with open("inventory.json", "r") as file:
            # Load the data from the JSON file
            data = json.load(file)

        print("Inventory loaded successfully.")

        #Get inventory and transaction history
        inventory = data.get("inventory", [])
        transaction_history = data.get("transaction_history", [])

        #Return the loaded data
        return inventory, transaction_history

    #If the file does not exist, start with empty inventory
    print("inventory.json not found. Starting with empty inventory.")

    return [], []

def save_inventory():
    #Create a dictionary containing inventory and transaction history
    data = {
        "inventory": inventory,
        "transaction_history": transaction_history
    }

    #Open inventory.json for writing
    with open("inventory.json", "w") as file:
        # Save the data as JSON
        json.dump(data, file, indent=4)

    print("Inventory saved successfully!")

def add_product():
    #Display the add product heading
    print("\nAdd New Product")

    #Ask for a valid product ID
    while True:
        product_id_input = input("Product ID: ").strip()

        # Convert the product ID to an integer
        try:
            product_id = int(product_id_input)
        except ValueError:
            print("Product ID must be a number.")
            continue

        # Check whether the product ID already exists
        product_exists = False

        for product in inventory:
            if product["id"] == product_id:
                product_exists = True
                break

        # Check for duplicate product ID
        if product_exists:
            print("Product ID already exists.")
            continue

        # Product ID is valid
        break

    #Ask for a valid product name
    while True:
        product_name = input("Product Name: ").strip()

        # Check that the product name is not empty
        if product_name == "":
            print("Product name cannot be empty.")
            continue

        # Product name is valid
        break

    #Ask for a valid product price
    while True:
        price_input = input("Price: ")

        # Convert the price to a decimal number
        try:
            price = float(price_input)
        except ValueError:
            print("Price must be a number.")
            continue

        # Check that the price is not negative
        if price < 0:
            print("Price cannot be negative.")
            continue

        # Price is valid
        break

    #Ask for a valid stock quantity
    while True:
        stock_input = input("Stock Quantity: ")

        # Convert the stock to an integer
        try:
            stock = int(stock_input)
        except ValueError:
            print("Stock quantity must be a number.")
            continue

        # Check that the stock is not negative
        if stock < 0:
            print("Stock quantity cannot be negative.")
            continue

        # Stock quantity is valid
        break

    #Create the new product dictionary
    new_product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    }

    #Add the new product to the inventory list
    inventory.append(new_product)

    #Record the transaction
    transaction_history.append({
        "product_id": product_id,
        "amount": stock
    })

    print("Product added successfully!")

def update_stock():
    #Ask the user for the product ID
    product_id_input = input("Product ID: ")

    #Convert the ID to an integer
    try:
        product_id = int(product_id_input)
    except ValueError:
        print("Product ID must be a number.")
        return

    #Search for the product
    for product in inventory:
        if product["id"] == product_id:

            #Ask how much stock to add
            quantity_input = input("Stock Quantity to Add: ")

            #Convert the quantity to an integer
            try:
                quantity = int(quantity_input)
            except ValueError:
                print("Stock quantity must be a number.")
                return

            #Check that the quantity is not negative
            if quantity < 0:
                print("Stock quantity cannot be negative.")
                return

            #Update the stock
            product["stock"] += quantity

            #Record the transaction
            transaction_history.append({
                "product_id": product_id,
                "amount": quantity
            })

            print("Stock updated successfully!")
            return

    #Product was not found
    print("Product not found.")

def search_product():
    #Ask for a valid product ID
    while True:
        product_id_input = input("Product ID to Search: ")

        #Convert the ID to an integer
        try:
            product_id = int(product_id_input)
        except ValueError:
            print("Product ID must be a number.")
            continue

        #Search through the inventory
        product_found = False

        for product in inventory:
            if product["id"] == product_id:

                # Display the product information
                print("\nProduct Found")
                print(
                    f"ID: {product['id']} | "
                    f"Name: {product['name']} | "
                    f"Price: ${product['price']:.2f} | "
                    f"Stock: {product['stock']}"
                )

                product_found = True
                break

        #Check if the product was found
        if product_found:
            break

        print("Product not found.")

def display_all():
    #Display the current inventory
    print("\nCurrent Inventory")
    print("-" * 64)

    #Check if the inventory is empty
    if not inventory:
        print("No products in inventory.")
    else:
        #Loop through every product
        for product in inventory:
            print(
                f"ID: {product['id']} | "
                f"Name: {product['name']} | "
                f"Price: ${product['price']:.2f} | "
                f"Stock: {product['stock']}"
            )

    print("-" * 64)

#Load inventory from inventory.json
inventory, transaction_history = load_inventory()

# Display the system heading
print("\n=======================================")
print("        INVENTORY MANAGEMENT SYSTEM")
print("=======================================")

# Main menu
while True:
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

    # Ask the user to choose an option
    option = input("Enter option: ")

    # Display all products
    if option == "1":
        display_all()

    # Add a new product
    elif option == "2":
        add_product()

    # Update product stock
    elif option == "3":
        update_stock()

    # Search for a product
    elif option == "4":
        search_product()

    # Save inventory to JSON
    elif option == "5":
        save_inventory()

    # Exit the program
    elif option == "6":
        print("Exiting Inventory Management System.")
        break

    # Handle invalid menu option
    else:
        print("Invalid option. Please choose 1-6.")