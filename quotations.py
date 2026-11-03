from customers import customers
from fleet import vehicles


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
    while True:
        cust_id = input("Enter Customer ID: ").strip().upper()
        for customer in customers:
            if cust_id == customer["customer_id"]:
                return customer
        else:
            print("This ID doesn't exist!")


def select_vehicle():
    while True:
        veh_id = input("Enter Vehicle ID: ").strip().upper()
        for vehicle in vehicles:
            if (veh_id == vehicle["vehicle_id"]):
                if vehicle['availability']:
                    return vehicle
                else:
                    print("This vehicle is currently unavailable!")
                    break
        else:
            print("Vehicle not found!")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the vehicle quantity: "))
        except ValueError:
            print("Please enter a valid whole number!")
            continue
        if quantity <= 0:
            print("Quantity can't be zero or negative!")
        else:
            return quantity