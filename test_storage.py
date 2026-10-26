from storage import *

fictional_customer = [{
        "customer_id": "C005",
        "company_name": "microsoft",
        "contact_name": "john smith",
        "phone_number": "01055698707",
        "email_address": "john_smith@gmail.com",
        "city": "new york"
    }]


save_customers(fictional_customer)
result = load_customers()
print(result)