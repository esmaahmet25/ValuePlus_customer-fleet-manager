def customer_menu():
    while True:
        print("""
            ValuePlus — Customer Management

            1. Add a Customer
            2. View All Customers
            3. Search for a Customer
            4. Return to Main Menu
        """)

        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            print("\nAdd a Customer selected.")
        elif user_choice == "2":
            print("\nView All Customers selected.")
        elif user_choice == "3":
            print("\nSearch for a Customer selected.")
        elif user_choice == "4":
            return
        else:
            print("\nInvalid choice! Please enter a valid choice.")