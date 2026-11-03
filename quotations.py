from customers import customers

def quotation_menu():
    while True:
        print("""
            ValuePlus — Quotations Management

            1. Create a Quotation
            2. View All Quotations
            3. Search for a Quotation
            4. Return to Main Menu
            5. Exit
        """)

        user_choice = input("Enter your choice (1-5): ")
        if user_choice == "1":
            print("\nAdd a Quotation selected.")
        elif user_choice == "2":
            print("\nView All Quotations selected.")
        elif user_choice == "3":
            print("\nSearch for a Quotation selected.")
        elif user_choice == "4":
            return False
        elif user_choice == "5":
            print("\nThank you for using ValuePlus Customer & Fleet Manager!\nGoodbye!")
            return True
        else:
            print("\nInvalid choice! Please enter a valid choice.")


def select_customer():
    #Ask the user to enter a Customer ID./Remove unnecessary spaces using .strip()./Convert the ID to uppercase using .upper().
    cust_id = input("Enter Customer ID: ").strip().upper()
    
    #Search through the customers list.
    for customer in customers:
        #Return the matching customer dictionary if found.
        if cust_id == customer["customer_id"]:
            return customer
    else:
        #Display an error message if the ID doesn't exist.
        print("This ID doesn't exist!")
