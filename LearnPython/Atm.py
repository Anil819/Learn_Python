import sys


user_data = {
    "account_number": "1234",
    "pin": "1234",
    "balance": 10000,
    "transactions": [],
}


def login():
    print(" Welcome in Atm ")
    acc = input("Enter Your Account NUmber")
    pin = input("Enter Your Account NUmber")
    if acc == user_data["account_number"] and user_data["pin"]:
        print("\n Login Successfully")
        main()
    else:
        print("\n Invalid User ")
        sys.exit()


def main():
    while True:
        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transaction_history()
        elif choice == "5":
            print("Thank you for using ATM!")
            sys.exit()
        else:
            print("Invalid choice, try again.")


def check_balance():
    print(f"Your Balance is: ₹{user_data['balance']}")


def deposit():
    Amount = float(input(" Enter Amount For Deposit : "))
    if Amount > 0:
        Amount = user_data["balance"] + Amount
        user_data["transactions"].append(f"Deposited ₹{Amount}")
        print(" Deposit Successfully ")
        main()
    else:
        print("Invalid , Please Try Again Later ")
    deposit()


def withdraw():
    Amount = float(input(" Enter Amount For Deposit : "))
    if Amount <= user_data["balance"]:
        Amount = user_data["balance"] - Amount
        user_data["transactions"].append(f"Withdrawl ₹{Amount}")
        print(" Withdrawl Successfully ")
        main()
    else:
        print("Invalid , Please Try Again Later ")
    withdraw()


def transaction_history():
    print("\n==== Transaction History ====")
    if not user_data["transactions"]:
        print("No transactions yet.")
    else:
        for t in user_data["transactions"]:
            print(t)

login()