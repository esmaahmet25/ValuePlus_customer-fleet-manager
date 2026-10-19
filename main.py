def main():

    while True:
        print("""
    ========================================
     ValuePlus Customer & Fleet Manager
    ========================================

    1. Customer Management
    2. Fleet Management
    3. Quotations
    4. Exit
"""
)
        user_choice = input("Enter your choice (1-4): ")
        if user_choice == "1":
            print("\nYou selected Customer Management.\n")
        elif user_choice == "2":
            print("\nYou selected Fleet Management.\n")
        elif user_choice == "3":
            print("\nYou selected Quotations.\n")
        elif user_choice == "4":
            print("\nThank you for using ValuePlus Customer & Fleet Manager!\nGoodbye!")
            break
        else:
            print("\nInvalid choice! Enter a valid number (1-4)")

if __name__== "__main__":
    main()