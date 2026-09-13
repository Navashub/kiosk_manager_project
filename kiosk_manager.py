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


def main():
    kiosk_name, owner_name = get_kiosk_info()
    print_welcome_banner(kiosk_name, owner_name)

    while True:
        show_menu()
        choice = get_menu_choice()

        if choice == 1:
            print("\n[View Stock will be built in feature 3]\n")
        elif choice == 2:
            print("\n[Add/Restock will be built in Feature 3]\n")
        elif choice == 3:
            print("\m[Sell a produt will be built in Feature 4]\n")
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