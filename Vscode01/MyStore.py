inventory = {
    1: {"name": "Rice", "price": 60, "quantity": 50},
    2: {"name": "Wheat", "price": 45, "quantity": 40},
    3: {"name": "Milk", "price": 30, "quantity": 25},
    4: {"name": "Sugar", "price": 40, "quantity": 20}
}


cart = {}

# -------------------- SELLER INTERFACE --------------------
def seller_menu():
    while True:
        print("\n--- Seller Menu ---")
        print("1. View Inventory")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Exit Seller Menu")


        choice = input("Enter choice: ")


        if choice == "1":
            view_inventory()
        # elif choice == "2":
        #     add_product()
        # elif choice == "3":
        #     update_stock()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

def view_inventory():
    print("\n----Invetory----")
    for pid, details in inventory.items():
        print(f"ID:{pid} | {details['name']} | Price:₹{details['price']} | Qty:{details['quantity']}")

seller_menu()