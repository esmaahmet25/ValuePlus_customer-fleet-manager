from customers import customers
from fleet import vehicles
from storage import load_quotations, save_quotations

quotations = load_quotations()


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
            create_quotation()
        elif user_choice == "2":
            view_all_quotations()
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


def get_contract_duration():
    while True:
        try:
            duration = int(input("Enter contract duration (months): "))
        except ValueError:
            print("Please enter a valid whole number!")
            continue
        if duration <= 0:
            print("Duration can't be zero or negative!")
        else:
            return duration


def calculate_totals(monthly_price, quantity, duration):
    monthly_total = monthly_price  * quantity
    contract_total = monthly_total * duration
    return monthly_total, contract_total



def generate_quotation_id():   
    quotation_numbers = []
    for quotation in quotations:
        quotation_number = int(quotation["quotation_id"][1:])
        quotation_numbers.append(quotation_number)
    if not quotation_numbers:
        quotation_id = "Q001"
    else:
        maxi_number = max(quotation_numbers) + 1
        quotation_id = (f"Q{maxi_number:03d}")
    return quotation_id



def create_quotation():
    quotation_id = generate_quotation_id()
    selected_customer = select_customer()
    selected_vehicle = select_vehicle()
    vehicle_quantity = get_quantity()
    contract_duration = get_contract_duration()

    price = selected_vehicle['monthly_lease_price']
    monthly_total, contract_total = calculate_totals(
        price, vehicle_quantity, contract_duration
        )

    quotation_info = {
        "quotation_id":	quotation_id,
        "customer_id": selected_customer["customer_id"],
        "vehicle_id": selected_vehicle["vehicle_id"],
        "quantity":	vehicle_quantity,
        "monthly_price": price,
        "contract_duration": contract_duration,
        "monthly_total": monthly_total,
        "contract_total": contract_total
    }

    quotations.append(quotation_info)
    save_quotations(quotations)

    print(f"""
        ========== Quotation Details ==========
        Quotation ID: {quotation_info["quotation_id"]}
        Customer ID: {quotation_info["customer_id"]}
        Vehicle ID: {quotation_info["vehicle_id"]}
        Quantity: {quotation_info["quantity"]}
        Contract duration: {quotation_info["contract_duration"]}
        Monthly total: {quotation_info["monthly_total"]:.2f} SAR
        Contract total: {quotation_info["contract_total"]:.2f} SAR
        ======================================
    """)    


def view_all_quotations():
    if not quotations:
        print("No quotations found!")
        return
    
    print("""
        ========== Quotations Details ==========
        """)
    for quotation in quotations: 
        print(f"""
            Quotation ID: {quotation["quotation_id"]}
            Customer ID: {quotation["customer_id"]}
            Vehicle ID: {quotation["vehicle_id"]}
            Quantity: {quotation["quantity"]}
            Monthly price: {quotation["monthly_price"]:.2f} SAR
            Contract duration: {quotation["contract_duration"]}
            Monthly total: {quotation["monthly_total"]:.2f} SAR
            Contract total: {quotation["contract_total"]:.2f} SAR
            -----------------------------------
    """)