def get_kiosk_info():
    kiosk_name = input("What's the name of your kiosk? ").strip().title()
    owner_name = input("What's your name? ").strip().title()
    return kiosk_name, owner_name

def print_welcome_banner(kiosk_name, owner_name):
    print(f"\nWelcome to {kiosk_name}'s Kiosk Manager, run by {owner_name}\n")

def main():
    kiosk_name, owner_name = get_kiosk_info()
    print_welcome_banner(kiosk_name, owner_name)


if __name__ == "__main__":
    main()