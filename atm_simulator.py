#ATM SIMULATOR
#class1-Account-balance, PIN
#class2-ATM-user login, the main menu, and switching accounts

#class1-Account
class Account: #create account class to save account data
    def __init__(self, acc_num, pin, balance):
        self.acc_num = acc_num
        self.pin = pin
        self.balance = float(balance)
        self.history = [f"Account opened with initial balance: ${self.balance:.2f}"]

    def check_balance(self): #another function to show balance
        print(f"\n Current Balance: ${self.balance:.2f}")

    def deposit(self, amount): #another function to deposit cash
        if amount <= 0:
            print("Amount must be greater than 0!")
        else:
            self.balance += amount
            self.history.append(f"Deposited: +${amount:.2f}")
            print(f"Successfully deposited ${amount:.2f}")
            print(f"New Balance: ${self.balance:.2f}")

    def withdraw(self, amount): #another function to withdraw cash
        if amount <= 0:
            print("Amount must be greater than 0!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.history.append(f"Withdrew: -${amount:.2f}")
            print(f"Successfully withdrew ${amount:.2f}")
            print(f"Remaining Balance: ${self.balance:.2f}")

    def show_history(self): #another function to show transaction history
        print(f"\n--- Account History #{self.acc_num} ---")
        for item in self.history:
            print(f"• {item}")


#class2-ATM class
class ATM:
    def __init__(self): #dictionary storing account details/objects)
        self.accounts = {
            "1001": Account("1001", "1234", 500.0),
            "1002": Account("1002", "4321", 1200.0)
        }

    def start(self): #ATM main run code
        print("!! Welcome to ATM Simulator !!")
        while True:
            acc_num = input("Enter Account Number or 'exit' to quit: ").strip()
            if acc_num.lower() == "exit":
                print("Thank you for using the ATM. Goodbye!")
                break

            if acc_num not in self.accounts:
                print("Account not found! Please try again.")
                continue

            # match the account
            user_account = self.accounts[acc_num]

            # verify PIN
            pin = input("Enter 4-digit PIN: ").strip()
            if pin != user_account.pin:
                print("Incorrect PIN! Access denied.")
            else:
                print(f"\nLogin successful! Welcome Account #{acc_num}")
                self.show_user_menu(user_account)

    def show_user_menu(self, account):
        while True: #show options of ATM
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transaction History")
            print("5. Log Out")

            choice = input("Choose an option (1-5): ").strip()
            if choice == "1":
                account.check_balance()

            elif choice == "2":
                try:
                    amount = float(input("Enter deposit amount: $"))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid input! Please enter numbers only.")

            elif choice == "3":
                try:
                    amount = float(input("Enter withdrawal amount: $"))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid input! Please enter numbers only.")

            elif choice == "4":
                account.show_history()

            elif choice == "5":
                print("\nLogging out... Done!")
                break

            else:
                print("Invalid option! Please pick between 1 and 5.")

#run classes
my_atm = ATM()
my_atm.start()