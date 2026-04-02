from tools.password_checker import check_password

while True:
    print("================================")
    print("Welcome to Genesis Cyber Toolkit")
    print("================================\n")
    print("Please select an option:")
    print("1. Password Strength Checker")
    print("2. Exit")
    print("\n")

    choice = input("Enter your choice: ")
    print("\n")

    if choice == '1':
        password = input("Enter a password to check its strength: ")
        result = check_password(password)
        print(result)

    elif choice == '2':
            print("Exiting the toolkit. Goodbye!")
            break   

else:
    print("Invalid choice. Please try again.\n")
