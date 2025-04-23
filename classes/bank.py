class Bank:
    def __init__(self, accountname, accountBalance, depositdetails, withdrawndetails, accounttype):
        self.__accountname = accountname
        self.__accountbalance = accountBalance
        self.__depositdetails = depositdetails
        self.__withdrawdetails = withdrawndetails
        self.__accounttype = accounttype

    def bank_functions(self):
        while True:
            print("\n--- Welcome to the Bank ---")
            print("1. Show Balance")
            print("2. Account Type")
            print("3. Money Transaction")
            print("4. Exit")

            choice = input("Choose an option (1-4): ").strip()

            if choice == "1":
                print(f"Current balance: ${self.__accountbalance:.2f}")

            elif choice == "2":
                print(f"Account type: {self.__accounttype}")

            elif choice == "3":
                self.user_transaction()

            elif choice == "4":
                print("Thank you for using our services!")
                break

            else:
                print("Invalid choice. Please try again.")

    def user_transaction(self):
        print("\n--- Transaction Menu ---")
        choice = input("Do you want to Deposit or Withdraw? ").strip().upper()

        if choice == 'DEPOSIT':
            amount = float(input("Enter amount to deposit: "))
            self.__accountbalance += amount
            self.__depositdetails = amount
            print(f"Successfully deposited ${amount:.2f}. New balance: ${self.__accountbalance:.2f}")

        elif choice == 'WITHDRAW':
            amount = float(input("Enter amount to withdraw: "))
            if amount > self.__accountbalance:
                print("Insufficient balance.")
            else:
                self.__accountbalance -= amount
                self.__withdrawdetails = amount
                print(f"Successfully withdrawn ${amount:.2f}. New balance: ${self.__accountbalance:.2f}")

        else:
            print("Invalid choice. Please type 'Deposit' or 'Withdraw'.")

bank = Bank('Meessam', 20000.0, 2000.0, 2000.0, 'Master card')


bank.bank_functions()
