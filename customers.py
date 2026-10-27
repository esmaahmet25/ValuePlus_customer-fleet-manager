from storage import load_customers, save_customers
customers = load_customers()


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
            add_customer()
        elif user_choice == "2":
            print("\nView All Customers selected.")
            view_customers()
        elif user_choice == "3":
            print("\nSearch for a Customer selected.")
            search_customer()
        elif user_choice == "4":
            return
        else:
            print("\nInvalid choice! Please enter a valid choice.")


def add_customer():
    customer_numbers = []
    for customer in customers:
        customer_number = int(customer["customer_id"][1:])
        customer_numbers.append(customer_number)
    if not customer_numbers:
        customer_id = "C001"
    else:
        maxi = max(customer_numbers) + 1
        customer_id = (f"C{maxi:03d}")

    company_name = input("Enter company name: ").strip()
    while not company_name:
        print("Company name shouldn't be empty!")
        company_name = input("Enter company name: ").strip()
    company_name = company_name.title()

    contact_name = input("Enter contact person's name : ").strip()
    while not contact_name:
        print("Please enter a contact name!")
        contact_name = input("Enter cintact person's name: ").strip()
    contact_name = contact_name.title()

    phone_number = input("Enter phone number : ").strip()
    while not phone_number:
        print("Phone number should not be empty!")
        phone_number = input("Enter phone number : ").strip()

    email_address = input("Enter email address : ").strip()    
    while True:
        if not email_address:
            print("Enter a valid email address!")
            email_address = input("Enter email address : ").strip()
        elif ("@" not in email_address) or ("." not in email_address):
            print("Enter a valid email address!")
            email_address = input("Enter email address : ").strip()
        else:
            break
    
    city = input("Enter city : ").strip().title()

    customer_info = {
        "customer_id": customer_id,
        "company_name": company_name,
        "contact_name": contact_name,
        "phone_number": phone_number,
        "email_address": email_address,
        "city": city
    }

    customers.append(customer_info)
    save_customers(customers)

    print(f"""
        ========== Customer Details ==========
        Customer ID: {customer_info["customer_id"]}
        Company Name: {customer_info["company_name"]}
        Contact Name: {customer_info["contact_name"]}
        Phone Number: {customer_info["phone_number"]}
        Email address: {customer_info["email_address"]}
        City: {customer_info["city"]}
        ======================================
    """
    )

    print(f"\nTotal customers: {len(customers)}")

    
def view_customers():
    if not customers:
        print("No customers found!")
        return
    print("""
           ========== Customer List ==========
    """)
    for customer in customers:
        print(f"""
            Customer ID: {customer["customer_id"]}
            Company Name: {customer["company_name"]}
            City: {customer["city"]}
            -----------------------------------
    """)
    

def search_customer():
    if not customers:
        print("No customers are registered!")
        return
    customer_id = input("Enter the customer ID: ").strip().upper()
    for customer in customers:
        if customer_id == customer["customer_id"]:
            print("""
                ========== Customer List ==========
            """)
            print(f"""
                Customer ID: {customer["customer_id"]}
                Company Name: {customer["company_name"]}
                City: {customer["city"]}
                -----------------------------------
        """)
            return
    print("Customer not found!")

