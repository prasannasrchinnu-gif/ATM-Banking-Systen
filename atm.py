# ATM Banking System in Python

balance = 10000
pin = "1234"
transactions = []

print("===== ATM BANKING SYSTEM =====")

user_pin = input("Enter your PIN: ")

if user_pin == pin:
    print("\nLogin Successful!")

    while True:
        print("\n------ MENU ------")
        print("1. Balance Enquiry")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Mini Statement")
        print("5. Change PIN")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Current Balance: ₹{balance}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            balance += amount
            transactions.append(f"Deposited ₹{amount}")
            print("Amount Deposited Successfully!")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= balance:
                balance -= amount
                transactions.append(f"Withdrawn ₹{amount}")
                print("Please collect your cash.")
            else:
                print("Insufficient Balance!")

        elif choice == "4":
            print("\n----- Mini Statement -----")
            if transactions:
                for t in transactions:
                    print(t)
            else:
                print("No transactions found.")
            print(f"Available Balance: ₹{balance}")

        elif choice == "5":
            new_pin = input("Enter New PIN: ")
            pin = new_pin
            print("PIN Changed Successfully!")

        elif choice == "6":
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid Choice!")

else:
    print("Incorrect PIN! Access Denied.")
