# Simple ATM Machine Program

# Initial values
pin = "1234"  # Default PIN
balance = 10000  # Initial balance

# Function to check PIN
def verify_pin():
    entered_pin = input("Enter your PIN: ")
    return entered_pin == pin

# Function for showing balance
def show_balance():
    print(f"Your current balance is: ₹{balance}")

# Function for withdrawing money
def withdraw_money():
    global balance
    amount = int(input("Enter the amount to withdraw: ₹"))
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"₹{amount} has been withdrawn. Your new balance is ₹{balance}")

# Function for depositing money
def deposit_money():
    global balance
    amount = int(input("Enter the amount to deposit: ₹"))
    balance += amount
    print(f"₹{amount} has been deposited. Your new balance is ₹{balance}")

# Function for changing PIN
def change_pin():
    global pin
    current_pin = input("Enter your current PIN: ")
    if current_pin == pin:
        new_pin = input("Enter your new PIN: ")
        confirm_pin = input("Confirm your new PIN: ")
        if new_pin == confirm_pin:
            pin = new_pin
            print("PIN changed successfully!")
        else:
            print("PINs do not match. Try again.")
    else:
        print("Incorrect current PIN.")

# ATM Menu
def atm_menu():
    while True:
        print("\nWelcome to the ATM")
        print("1. Withdraw Money")
        print("2. Show Balance")
        print("3. Deposit Money")
        print("4. Change PIN")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            if verify_pin():
                withdraw_money()
            else:
                print("Incorrect PIN.")
        elif choice == "2":
            if verify_pin():
                show_balance()
            else:
                print("Incorrect PIN.")
        elif choice == "3":
            if verify_pin():
                deposit_money()
            else:
                print("Incorrect PIN.")
        elif choice == "4":
            if verify_pin():
                change_pin()
            else:
                print("Incorrect PIN.")
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the ATM menu
atm_menu()