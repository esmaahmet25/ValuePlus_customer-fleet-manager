from storage import load_vehicles, save_vehicles
vehicles = load_vehicles()

def fleet_menu():
    while True:
        print("""
            ValuePlus — Fleet Management

            1. Add a Vehicle
            2. View All Vehicles
            3. Search for a Vehicle
            4. Return to Main Menu
            5. Exit
        """)

        user_choice = input("Enter your choice (1-5): ")
        if user_choice == "1":
            print("\nAdd a Vehicle selected.")
            #add_vehicle()
        elif user_choice == "2":
            print("\nView All Vehicles selected.")
            #view_vehicles()
        elif user_choice == "3":
            print("\nSearch for a Vehicle selected.")
            #search_vehicle()
        elif user_choice == "4":
            return False
        elif user_choice == "5":
            print("\nThank you for using ValuePlus Customer & Fleet Manager!\nGoodbye!")
            return True
        else:
            print("\nInvalid choice! Please enter a valid choice.")



def add_vehicle():   
    vehicle_numbers = []
    for vehicle in vehicles:
        vehicle_number = int(vehicle["vehicle_id"][1:])
        vehicle_numbers.append(vehicle_number)
    if not vehicle_numbers:
        vehicle_id = "V001"
    else:
        maxi = max(vehicle_numbers) + 1
        vehicle_id = (f"V{maxi:03d}")

    while True:
        make = input("Enter vehicle make: ").strip().title()
        if not make:
            print("Make section can't be empty!")
        else:
            break

    while True:    
        model = input("Enter vehicle model: ").strip().title()
        if not model:
            print("Model section can't be empty!")
        else:
            break

    while True:
        try:
            year = int(input("Enter manufacturing year: "))
        except ValueError:
            print("Manufacturing year should be a number!")
            continue

        if not (2000 <= year <= 2026):
            print("Manufacturing year must be between 2000 and 2026!")
        else:
            break

    while True:
        registration_number = input("Enter registration number: ").strip().upper()
        if not registration_number:
            print("Registration number can't be empty!")
            continue

        registration_number_exists = False
        for vehicle in vehicles:
            if vehicle["registration_number"] == registration_number:
                registration_number_exists = True
                break
        if registration_number_exists:
            print("A vehicle with this registration number already exists!")
            continue

        else:
            break

    while True:
        try:
            monthly_lease_price = float(input("Enter vehicle monthly_lease_price: ").strip())
        except ValueError:
            print("The monthly lease price should be a number!")
            continue
        
        if not monthly_lease_price > 0:
            print("Monthly lease price must be greater than zero.")
        else:
            break

    availability = True
    print(f"Availability: {'Available' if availability else 'Unavailable'}") 

    
    vehicle_info = {
        "vehicle_id": vehicle_id,
        "make": make,
        "model": model,
        "year": year,
        "registration_number": registration_number,
        "monthly_lease_price": monthly_lease_price,
        "availability": availability
}
    vehicles.append(vehicle_info)
    
    save_vehicles(vehicles)

    print(f"""
        ========== Vehicles Details ==========
        Vehicle ID: {vehicle_info["vehicle_id"]}
        Make: {vehicle_info["make"]}
        Model: {vehicle_info["model"]}
        Year: {vehicle_info["year"]}
        Registration number: {vehicle_info["registration_number"]}
        Monthly lease price: {vehicle_info["monthly_lease_price"]:.2f} SAR
        Availability: {vehicle_info["availability"]}
        ======================================
    """
    )

    print(f"\nTotal vehicles: {len(vehicles)}")