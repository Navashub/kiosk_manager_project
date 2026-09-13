def get_kiosk_info():
    kiosk_name = input("What's the name of your kiosk? ").strip().title()
    owner_name = input("What's your name? ").strip().title()
    return kiosk_name, owner_name


def print_welcome_banner(kiosk_name, owner_name):
    print(f"\nWelcome to {kiosk_name}'s Kiosk Manager, run by {owner_name}\n")


def show_menu():
    print("=== MAIN MENU ===")
    print("1. View Stock")
    print("2. Add/Restock a Product")
    print("3. Sell a Product")
    print("4. View Sales Report")
    print("5. Search Products")
    print("6. Exit")


def get_menu_choice():
    choice = input("Enter your choice: ").strip()
    if choice.isdigit():
        return int(choice)
    return None 


def create_default_inventory():
    return {
        "Bread": {"price": 65, "quantity": 20},
        "Milk": {"price": 60, "quantity": 15},
        "Eggs": {"price": 15, "quantity": 30},
        "Sugar": {"price": 150, "quantity": 10}
    }


def view_stock(stock):
    print("\n------ CURRENT STOCK ------")
    print(f"{'Product':<15}{'Price (KES)':<15}{'Quantity':<10}")
    for name, details in stock.items():
        print(f"{name:<15}{details['price']:<15}{details['quantity']:<10}")
    print()   


def restock_product(stock):
    name = input("Which product? ").strip().title()
    qty_input = input("How many units to add? ").strip()

    if not qty_input.isdigit():
        print("\nPlease enter a valid whole number for quantity.\n")
        return 

    qty = int(qty_input)

    if name in stock:
        stock[name]["quantity"] += qty
        print(f"\nRestocked {qty} units of {name}. New quantity: {stock[name]['quantity']}\n")
    else:
        price_input = input(f"{name} is new. What's the price (KES)? ").strip()
        if not price_input.isdigit():
            print("\nPlease enter a valid whole number for price. Product not added.\n")
            return 
        price = int(price_input)
        stock[name] = {"price": price, "quantity": qty}
        print(f"\nAdded new product {name}: {qty} unity at KES {price}each.\n")     


def sell_product(stock, sales_log, items_sold):
    name = input("Which product? ").


def main():
    kiosk_name, owner_name = get_kiosk_info()
    print_welcome_banner(kiosk_name, owner_name)

    stock = create_default_inventory()

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 1:
            view_stock(stock)
        elif choice == 2:
            restock_product(stock)
        elif choice == 3:
            print("\n[Sell a produt will be built in Feature 4]\n")
        elif choice == 4:
            print("\n[Sales Report will be built in Feature 5]\n")
        elif choice == 5:
            print("\n[Search Products will be built in Feature 6]\n")
        elif choice == 6:
            print(f"\nSaving data... Goodbye, {owner_name}!")
            break 
        else:
            print("\nSorry, that's not a vlaid choice. Please try again.\n")

if __name__ == "__main__":
    main()