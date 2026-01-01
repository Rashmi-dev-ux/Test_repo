#--------------------Kirana Store CLI-------------------
stock = [
    {"name": "Rice", "price": 60, "quantity": 50},
    {"name": "Wheat", "price": 45, "quantity": 40},
    {"name": "Milk", "price": 30, "quantity": 25},
    {"name": "Sugar", "price": 40, "quantity": 20}
   ]
def view_stock():
    
    for i,item in enumerate(stock):
        print(f"{i+1}.  {item['name']}   $ {str(item['price'])} /kg     {str(item['quantity'])}")



def add_stock():
    print("\n========Add/Update stock========")
    view_stock()

    choice = int(input("Enter the product number between(1-4): "))
    add_quantity = int(input("\n Enter quantity to add: "))

    new_quantity = stock[choice - 1]["quantity"] + add_quantity

    print(f"Added {add_quantity}. New stock: {new_quantity}")
    

def remove_stock():
    print("====Remove Stock====")
    view_stock()

    choice = int(input("Enter the product number between(1-4): "))
    remove_quantity = int(input("\n Enter quantity to remove: "))

    new_quantity = stock[choice - 1]["quantity"] - remove_quantity

    print(f"Removed {remove_quantity}. New stock: {new_quantity}")

def buy_product():
    print("=====Add to Cart=====")
    view_stock()

    choice = int(input("Enter the product number between(1-4) to add products to cart: "))
    quantity_to_add = int(input("\n Enter the quantity to add: "))

    if quantity_to_add > stock[choice - 1]["quantity"]:
        print("Sorry, not enough stock")
    
    else:
        stock[choice - 1]["quantity"] -= quantity_to_add
        print(f"Purchased {quantity_to_add} kg {stock[choice - 1]['name']}")




def seller_login(): #After logging into seller menu
    print("\n======seller menu======")
    print("1. View Stock")
    print("2. Add stock")
    print("3. Remove stock")
    print("4. Back to Main Menu")

    while True:

        choice = input("Option: ")
        if choice == "1":
            view_stock()
        elif choice == "2":
            add_stock()
        elif choice == "3":
            remove_stock()
        elif choice == "4":
            print("Thanks!!")
            break
            
        else:
            print("Oops! Invalid selection")


def customer_shopping():
    print("======Customer Shopping=======")
    while True:
        print("-------Customer Menu---------")
        print("1. View Products")
        print("2. Buy Product")
        print("3. Exit")

        choice = int(input("Choose: "))
        if choice == 1:
            view_stock()
        elif choice == 2:
            buy_product()
        elif choice == 3:
            print("Thanks for Visiting!")
            break
        else:
            print("Invalid Selection")


def main_loop():
    print("==============KIRANA STORE==============")
    while True:
        print("-------Main Menu---------")
        print("1. Seller Login")
        print("2. Customer Shopping")
        print("3. Exit")

        choice = input("Choose: ")
        if choice == "1":
            seller_login()
        elif choice == "2":
            customer_shopping()
        elif choice == "3":
            print("Thank you :)")
            break
        else:
            print("Invalid Option")






#print("This is the main application")
if __name__ == "__main__":
    print(__name__)
    print("This is the main application")

    main_loop()

