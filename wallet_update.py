import csv
import os

# File paths for CSV files
users_file = 'users.csv'
wallets_file = 'wallets.csv'
transactions_file = 'transactions.csv'

class User:
    users = {}

    @staticmethod
    def load_data():
        if os.path.exists(users_file):
            with open(users_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    username, password = row
                    User.users[username] = User(username, password)

    @staticmethod
    def save_data():
        with open(users_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for user in User.users.values():
                writer.writerow([user.username, user.password])

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.wallet = Wallet(username)
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    @staticmethod
    def signup():
        print("Sign Up")
        username = input("Enter a username: ")
        if username in User.users:
            print("Username already exists. Please try a different one.")
            return
        
        password = input("Enter a password: ")
        user = User(username, password)
        User.users[username] = user
        user.wallet.save_data()
        print("Sign up successful! Logging you in...")

        # Call login function immediately after sign up
        User.login(username, password)

    @staticmethod
    def login(username=None, password=None):
        print("Log In")

        if username is None:
            username = input("Enter your username: ")

        if password is None:
            password = input("Enter your password: ")

        if username not in User.users:
            print("Username not found. Please sign up first.")
            return

        user = User.users[username]
        if user.password == password:
            print("Login successful!")
            user.dashboard()  # Call the wallet function after successful login
        else:
            print("Incorrect password. Please try again.")

    def dashboard(self):
        print(f"Welcome to your wallet, {self.username}!")

        while True:
            print("\nPlease select an option:")
            print("1. Send money")
            print("2. View balance")
            print("3. View transactions")
            print("4. Deposit money")
            print("5. Logout")

            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == '1':
                self.wallet.send_money()
            elif choice == '2':
                self.wallet.view_balance()
            elif choice == '3':
                self.wallet.view_transactions()
            elif choice == '4':
                self.wallet.deposit_money()
            elif choice == '5':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please select a valid option.")

class Wallet:
    wallets = {}

    @staticmethod
    def load_data():
        if os.path.exists(wallets_file):
            with open(wallets_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    username, balance = row
                    Wallet.wallets[username] = Wallet(username, float(balance))

    @staticmethod
    def save_data():
        with open(wallets_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for wallet in Wallet.wallets.values():
                writer.writerow([wallet.username, wallet.balance])

    def __init__(self, username, balance=400.0):
        self.username = username
        self.balance = balance
        Wallet.wallets[username] = self

    def send_money(self):
        recipient_username = input("Enter the recipient's username: ")
        if recipient_username not in User.users:
            print("Recipient not found.")
            return

        try:
            amount = float(input("Enter the amount to send: ₦"))
            if amount <= 0:
                print("Amount must be positive.")
                return
        except ValueError:
            print("Invalid amount.")
            return

        if self.balance < amount:
            print("Insufficient balance.")
            return

        recipient = User.users[recipient_username]
        self.balance -= amount
        recipient.wallet.balance += amount

        transaction = Transaction(self.username, recipient_username, amount)
        User.users[self.username].add_transaction(transaction)
        recipient.add_transaction(transaction)

        print(f"Sent ₦{amount} to {recipient_username} successfully.")

    def view_balance(self):
        print(f"Your current balance is: ₦{self.balance}")

    def view_transactions(self):
        user = User.users[self.username]
        if not user.transactions:
            print("No transactions found.")
            return

        print("ID  Your transactions:")
        for txn in user.transactions:
            print(f"{txn.id}. {txn.details()}")

        try:
            txn_id = int(input("Enter the transaction ID to view details or 0 to return: "))
            if txn_id == 0:
                return
            txn = next((t for t in user.transactions if t.id == txn_id), None)
            if txn:
                print(f"Transaction {txn_id}: {txn.details()}")
            else:
                print("Transaction ID not found.")
        except ValueError:
            print("Invalid input.")

    def deposit_money(self):
        try:
            amount = float(input("Enter the amount to deposit: ₦"))
            if amount <= 0:
                print("Amount must be positive.")
                return
        except ValueError:
            print("Invalid amount.")
            return

        self.balance += amount
        transaction = Transaction(self.username, self.username, amount, deposit=True)
        User.users[self.username].add_transaction(transaction)
        print(f"Deposited ₦{amount} successfully.")

class Transaction:
    id_counter = 1

    @staticmethod
    def load_data():
        if os.path.exists(transactions_file):
            with open(transactions_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    username, txn_id, txn_details = row
                    user = User.users[username]
                    txn = Transaction.from_string(txn_details, int(txn_id))
                    user.add_transaction(txn)
                    if Transaction.id_counter <= txn.id:
                        Transaction.id_counter = txn.id + 1

    @staticmethod
    def save_data():
        with open(transactions_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for user in User.users.values():
                for txn in user.transactions:
                    writer.writerow([user.username, txn.id, txn.details()])

    def __init__(self, sender, recipient, amount, deposit=False):
        self.id = Transaction.id_counter
        Transaction.id_counter += 1
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.deposit = deposit

    def details(self):
        if self.deposit:
            return f"Deposited ₦{self.amount}"
        return f"Sent ₦{self.amount} to {self.recipient}"

    @staticmethod
    def from_string(details, txn_id):
        parts = details.split()
        amount = float(parts[1][1:])
        if parts[0] == "Deposited":
            return Transaction(parts[0], parts[0], amount, deposit=True)
        return Transaction(parts[2], parts[-1], amount)

def main_menu():
    User.load_data()
    Wallet.load_data()
    Transaction.load_data()

    while True:
        print("\nPlease select an option:")
        print("1. Sign up")
        print("2. Login")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            User.signup()
        elif choice == '2':
            User.login()
        elif choice == '3':
            print("Please Login into your wallet.")
        elif choice == '4':
            print("Please Login into your wallet.")
        elif choice == '5':
            User.save_data()
            Wallet.save_data()
            Transaction.save_data()
            exit_program()
        else:
            print("Invalid choice. Please select a valid option.")

def exit_program():
    print("Exiting the program.")
    exit()

if __name__ == "__main__":
    main_menu()
