from customers import customer_menu

def display_menu():
    print("""
    ========================================
       ValuePlus Customer & Fleet Manager
    ========================================

    1. Customer Management
    2. Fleet Management
    3. Quotations
    4. Exit
"""
)

def handle_user_choice(user_choice):
        if user_choice == "1":
            print("\nYou selected Customer Management.\n")
            customer_menu()
            return False
        elif user_choice == "2":
            print("\nYou selected Fleet Management.\n")
            return False
        elif user_choice == "3":
            print("\nYou selected Quotations.\n")
            return False
        elif user_choice == "4":
            print("\nThank you for using ValuePlus Customer & Fleet Manager!\nGoodbye!")
            return True
        else:
            print("\nInvalid choice! Enter a valid number (1-4)")
            return False


def main(): 
    while True:
        display_menu()
        user_choice = input("Enter your choice (1-4): ")
        result = handle_user_choice(user_choice)
        if result:
            break
if __name__== "__main__":
    main()