import quotations

original_customers = quotations.customers.copy()
original_vehicles = quotations.vehicles.copy()


# Test 1: Create quotation without customers
quotations.customers.clear()

print("\n--- Testing Quotation Creation Without Customers ---")
quotations.create_quotation()


# Test 2: Create quotation without vehicles
quotations.customers.extend(original_customers)
quotations.vehicles.clear()

print("\n--- Testing Quotation Creation Without Vehicles ---")
quotations.create_quotation()


# Test 3: Select customer from an empty list
quotations.customers.clear()

print("\n--- Testing Empty Customer List ---")
customer = quotations.select_customer()
print("Returned value:", customer)


# Test 4: Select vehicle from an empty list
quotations.customers.extend(original_customers)

print("\n--- Testing Empty Vehicle List ---")
vehicle = quotations.select_vehicle()
print("Returned value:", vehicle)


# Restore original data
quotations.vehicles.extend(original_vehicles)

print("\nOriginal data restored in memory!")