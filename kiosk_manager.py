import os 

INVENTORY_FILE = "inventory.txt"
SALES_LOG_FILE = "sales_log.txt"


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

def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        return create_default_inventory()

    stock = {}
    with open(INVENTORY_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, price, quantity = line.split(",")
            stock[name] = {"price": int(price), "quantity": int(quantity)}
    return stock


def save_inventory(stock):
    with open(INVENTORY_FILE, "w") as f:
        for name, details in stock.items():
            f.write(f"{name}, {details['price']}, {details['quantity']}\n")

def save_sales_log(sales_log):
    with open(SALES_LOG_FILE, "a") as f:
        for name, qty, total in sales_log:
            f.write(f"{name}, {qty}, {total}\n")


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
    name = input("Which product? ").strip().title()

    if name not in stock:
        print(f"\nSorry, {name} is not in stock.\n")
        return 

    qty_input = input("How many units? ").strip()
    if not qty_input.isdigit():
        print("\nPlease enter a valid whole number for quantity.\n")
        return 

    qty = int(qty_input)

    if qty <= 0:
        print("\nQuantity must be greater than zero.\n")


    if stock[name]["quantity"] < qty:
        print(f"\nNot enough stock. Only {stock[name]['quantity']} units of {name} left.\n")
        return 

    stock[name]["quantity"] -= qty 
    total = stock[name]["price"] * qty 

    sales_log.append((name, qty, total))
    items_sold.add(name)

    print(f"\nSold {qty} {name} for KES {total}.\n")


def print_sales_report(sales_log, items_sold):
    if not sales_log:
        print("\nNo sales recorded yet today")
        return

    print("\n----- SALES REPORT -----")
    print(f"{'Product':<15}{'Qty':<10}{'Total (KES)':<15}")

    total_revenue = 0
    quantity_by_product = {}

    for name, qty, total in sales_log:
        print(f"{name:<15}{qty:<10}{total:<15}")
        total_revenue += total
        quantity_by_product[name] = quantity_by_product.get(name, 0) + qty 

    best_seller = max(quantity_by_product, key=quantity_by_product.get)

    print(f"\nTotal revenue: KES {total_revenue}")
    print(f"Unique products sold: {len(items_sold)}")
    print(f"Best-selling product: {best_seller} ({quantity_by_product[best_seller]} units)\n")


def search_products(stock):
    term = input("Search for a product: ").strip().lower()

    matches = {name: details for name, details in stock.items() if term in name.lower()}

    if not matches: 
        print("\nNo matches found.\n")
        return 

    print("\n----- SEARCH RESULTS -----")
    print(f"{'Product':<15}{'Price (KES)':<15}{'Quantity':<10}")
    for name, details in matches.items():
        print(f"{name:<15}{details['price']:<15}{details['quantity']:<10}")
    print()


def main():
    kiosk_name, owner_name = get_kiosk_info()
    print_welcome_banner(kiosk_name, owner_name)

    stock = create_default_inventory()
    sales_log = []
    items_sold = set()

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 1:
            view_stock(stock)
        elif choice == 2:
            restock_product(stock)
        elif choice == 3:
            sell_product(stock, sales_log, items_sold)
        elif choice == 4:
            print_sales_report(sales_log, items_sold)
        elif choice == 5:
            search_products(stock)
        elif choice == 6:
            save_inventory(stock)
            save_sales_log(sales_log)
            print(f"\nSaving data... Goodbye, {owner_name}")
            break 
        else:
            print("\nSorry, that's not a vlaid choice. Please try again.\n")

if __name__ == "__main__":
    main()