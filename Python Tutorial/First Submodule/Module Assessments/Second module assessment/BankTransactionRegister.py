import uuid
import datetime

class Transaction:
    def __init__(self, transaction_type, amount, balance_after):
        self.transaction_type = transaction_type
        self.amount = amount
        self.balance_after = balance_after
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        sign = "+" if self.amount > 0 else ""
        return f"{self.timestamp} | {self.transaction_type}: {sign}${self.amount:.2f} | Balance: ${self.balance_after:.2f}"

class BankAccount:
    def __init__(self, name, account_type, balance=0.0):
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.account_number = str(uuid.uuid4().int)[:8]
        self.transactions = []
        self.filename = f"{self.account_number}_{self.account_type}_{self.name}.txt"

        with open(self.filename, "w") as file:
            file.write(f"Account created for {self.name}\n")
            file.write(f"Account Number: {self.account_number}\n")
            file.write(f"Account Type: {self.account_type}\n")
            file.write(f"Initial Balance: ${self.balance:.2f}\n")
            file.write("-" * 40 + "\n")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        transaction = Transaction("Deposit", amount, self.balance)
        self._save_transaction(transaction)
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        transaction = Transaction("Withdrawal", -amount, self.balance)
        self._save_transaction(transaction)
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def _save_transaction(self, transaction):
        self.transactions.append(transaction)
        with open(self.filename, "a") as file:
            file.write(str(transaction) + "\n")

    def show_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def show_transactions(self):
        print("\n--- TRANSACTION HISTORY ---")
        try:
            with open(self.filename, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No transaction history found for this account.")

class TransactionRegister:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        name = input("Enter your name: ")
        account_type = input("Enter account type (Chequing/Savings): ")
        initial_balance = float(input("Enter initial deposit amount: "))
        account = BankAccount(name, account_type, initial_balance)
        self.accounts[account.account_number] = account
        print(f"\nAccount created successfully!")
        print(f"Account Number: {account.account_number}")
        print(f"File: {account.filename}")
        return account

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def find_account_by_name(self, name):
        results = [acc for acc in self.accounts.values() if acc.name.lower() == name.lower()]
        return results
    
    def show_all_balances(self):
        if not self.accounts:
            print("No accounts available.")
            return
        print("\n--- ALL ACCOUNT BALANCES ---")
        for acc in self.accounts.values():
            print(f"{acc.name} ({acc.account_type}) - Account Number: {acc.account_number} | Balance: ${acc.balance:.2f}")

    def run(self):
        print("Welcome to the Bank Transaction Register")
        while True:
            print("\n--- MAIN MENU ---")
            print("1. Create New Account")
            print("2. Use Existing Account")
            print("3. Show all Account Balances")
            print("4. Find Account by Name")
            print("5. Exit")

            choice = input("Enter choice (1-5): ")

            if choice == "1":
                account = self.create_account()
                self.manage_account(account)
            elif choice == "2":
                acc_num = input("Enter account number: ")
                account = self.find_account(acc_num)
                if account:
                    self.manage_account(account)
                else:
                    print("Account not found.")
            elif choice == "3":
                self.show_all_balances()
            elif choice == "4":
                search_name = input("Enter name: ")
                results = self.find_account_by_name(search_name)
                if results:
                    print(f"\nFound {len(results)} account(s): ")
                    for acc in results:                    
                        print(f"Account found: {acc.name} ({acc.account_type}) - Account Number: {acc.account_number} Balance: ${acc.balance:.2f}")
                else:
                    print("Name not found.")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def manage_account(self, account):
        while True:
            print(f"\n--- ACCOUNT MENU ({account.account_number}) ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Balance")
            print("4. Show Transaction History")
            print("5. Show all Account Balances")
            print("6. Back to Main Menu")

            choice = input("Enter choice (1-6): ")

            if choice == "1":
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == "3":
                account.show_balance()
            elif choice == "4":
                account.show_transactions()
            elif choice == "5":
                self.show_all_balances()
            elif choice == "6":
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    transaction_register = TransactionRegister()
    transaction_register.run()
