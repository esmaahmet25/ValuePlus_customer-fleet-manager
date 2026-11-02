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
