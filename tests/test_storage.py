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

from storage import load_quotations, save_quotations

# Test 1: Load quotations
quotations = load_quotations()
print("Initial quotations:", quotations)

# Test 2: Save a sample quotation
sample_quotation = {
    "quotation_id": "Q001",
    "customer_id": "C002",
    "vehicle_id": "V001",
    "quantity": 3,
    "monthly_price": 2500.00,
    "contract_duration": 12,
    "monthly_total": 7500.00,
    "contract_total": 90000.00
}

quotations.append(sample_quotation)
save_quotations(quotations)

# Test 3: Load the saved quotation
saved_quotations = load_quotations()
print("Saved quotations:", saved_quotations)