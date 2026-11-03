from quotations import generate_quotation_id, quotations

# Test 1: Empty quotation list
quotations.clear()
print("Test 1:", generate_quotation_id())

# Test 2: Two existing quotations
quotations.extend([
    {"quotation_id": "Q001"},
    {"quotation_id": "Q002"}
])
print("Test 2:", generate_quotation_id())

# Test 3: A gap in the quotation IDs
quotations.clear()
quotations.extend([
    {"quotation_id": "Q001"},
    {"quotation_id": "Q002"},
    {"quotation_id": "Q009"}
])
print("Test 3:", generate_quotation_id())