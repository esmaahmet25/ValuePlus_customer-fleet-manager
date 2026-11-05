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
            5. Exit
        """)

        user_choice = input("Enter your choice (1-5): ")
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
            return False
        elif user_choice == "5":
            print("\nThank you for using ValuePlus Customer & Fleet Manager!\nGoodbye!")
            return True
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

    invalid_company = ["none", "n/a", "null", "empty"]
    while True:
        company_name = input("Enter company name: ").strip().title()
        if not company_name:
            print("Company name shouldn't be empty!")
        elif company_name.lower() in invalid_company:
            print("Enter a valid company name!")
        else:
            break

    invalid_name = ["none", "n/a", "null", "empty"]    
    while True:
        contact_name = input("Enter contact person's name : ").strip().title()
        if not contact_name:
            print("Please enter a contact name!")
        elif contact_name.lower() in invalid_name:
            print("Enter a valid contact name!")
        else:
            break

    while True:
        phone_number = input("Enter the phone number: ").strip().replace(" ", "").replace("-", "")
        is_supported_format = False
        if phone_number.startswith("+966"):
            is_supported_format = True     
        elif phone_number.startswith("966"):
            phone_number = f"+{phone_number}"
            is_supported_format = True
        elif phone_number.startswith("05"):
            phone_number = f"+966{phone_number.removeprefix("0")}"
            is_supported_format = True

        if is_supported_format and (len(phone_number[4:]) == 9) and (phone_number[4:].isdigit() and phone_number[4:].startswith("5")):
            phone_exists = False
            for customer in customers:
                if customer["phone_number"] == phone_number:
                    phone_exists = True
                    break

            if phone_exists:
                print("A customer with this phone number already exists!")
                continue
            else:
                break    
        else:
            print("Unknown/Invalid format!")
            continue      

    
    while True:
        email_address = input("Enter email address : ").strip()
        if not email_address:
            print("Email address can't be empty!")
            continue
        
        elif ("@" not in email_address) or ("." not in email_address):
            print("Enter a valid email address!")
            continue

        elif email_address.count("@") != 1:
            print("Enter a valid email address!")
            continue

        local_part, domain = email_address.split("@")
        if (not local_part) or (".." in local_part) or (domain.startswith(".")) or (domain.endswith(".")) or (".." in domain) or ("," in email_address) or (any(char.isspace() for char in email_address)):
            print("Enter a valid email address!")
            continue

        
        email_exists = False
        for customer in customers:
            if customer["email_address"].lower() == email_address.lower():
                email_exists = True
                break

        if email_exists:
            print("A customer with this email already exists!")
            continue

        else:
            break 

    invalid_city = ["none", "n/a", "null", "empty"]    
    while True:
        city = input("Enter city : ").strip().title()
        if not city:
            print("City should not be empty!")
        elif city.lower() in invalid_city:
            print("Enter a valid city name!")
        else:
            break

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
           ========== Customer Details ==========
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