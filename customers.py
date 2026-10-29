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
        contact_name = input("Enter contact person's name: ").strip()
    contact_name = contact_name.title()

    while True:
        phone_number = input("Enter the phone number: ").strip().replace(" ", "")
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
            break
        else:
            print("Unknown/Invalid format!")
            

    email_address = input("Enter email address : ").strip()    
    while True:
        if not email_address:
            print("Email address can't be empty!")
            email_address = input("Enter email address : ").strip()
        
        elif ("@" not in email_address) or ("." not in email_address):
            print("Enter a valid email address!")
            email_address = input("Enter email address : ").strip()
        
        elif email_address.count("@") != 1:
            print("Enter a valid email address!")
            email_address = input("Enter email address : ").strip()
            continue

        local_part, domain = email_address.split("@")
        if (not local_part) or (domain.startswith(".")) or (domain.endswith(".")) or (".." in domain) or ("," in email_address) or (any(char.isspace() for char in email_address)):
            print("Enter a valid email address!")
            email_address = input("Enter email address : ").strip()
            continue

        else:
            break

    email_exists = False
    for customer in customers:
        if customer["email_address"].lower() == email_address.lower():
            email_exists = True
            break
    if email_exists:
        print("A customer with this email already exists!")
        return
   
    city = input("Enter city : ").strip()
    while not city:
        print("Please enter City name!")
        city = input("Enter city: ").strip()
    city = city.title()


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