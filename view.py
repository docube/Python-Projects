# view.py
from model import User, Wallet, Transaction
from repo import Repository


class WalletApp:
    def __init__(self):
        self.users = Repository.load_users()
        self.wallets = Repository.load_wallets()
        Repository.load_transactions(self.users)

    def signup(self):
        print("Sign Up")
        username = input("Enter a username: ")
        if username in self.users:
            print("Username already exists. Please try a different one.")
            return
        
        password = input("Enter a password: ")
        user = User(username, password)
        self.users[username] = user
        self.wallets[username] = user.wallet
        print("Sign up successful! Logging you in...")
        self.login(username, password)

    def login(self, username=None, password=None):
        print("Log In")

        if username is None:
            username = input("Enter your username: ")

        if password is None:
            password = input("Enter your password: ")

        if username not in self.users:
            print("Username not found. Please sign up first.")
            return

        user = self.users[username]
        if user.password == password:
            print("Login successful!")
            self.dashboard(user)  # Call the wallet function after successful login
        else:
            print("Incorrect password. Please try again.")

    def dashboard(self, user):
        print(f"Welcome to your wallet, {user.username}!")

        while True:
            print("\nPlease select an option:")
            print("1. Transfer")
            print("2. View balance")
            print("3. View transactions")
            print("4. Deposit money")
            print("5. Logout")

            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == '1':
                self.send_money(user)
            elif choice == '2':
                self.view_balance(user)
            elif choice == '3':
                self.view_transactions(user)
            elif choice == '4':
                self.deposit_money(user)
            elif choice == '5':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def send_money(self, sender):
        recipient_username = input("Enter the recipient's username: ")
        if recipient_username not in self.users:
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

        if sender.wallet.balance < amount:
            print("Insufficient balance.")
            return

        recipient = self.users[recipient_username]
        sender.wallet.balance -= amount
        recipient.wallet.balance += amount

        transaction = Transaction(sender.username, recipient_username, amount)
        sender.transactions.append(transaction)
        recipient.transactions.append(transaction)

        print(f"Sent ₦{amount} to {recipient_username} successfully.")

    def view_balance(self, user):
        print(f"Your current balance is: ₦{user.wallet.balance}")

    def view_transactions(self, user):
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

    def deposit_money(self, user):
        try:
            amount = float(input("Enter the amount to deposit: ₦"))
            if amount <= 0:
                print("Amount must be positive.")
                return
        except ValueError:
            print("Invalid amount.")
            return

        user.wallet.balance += amount
        transaction = Transaction(user.username, user.username, amount, deposit=True)
        user.transactions.append(transaction)
        print(f"Deposited ₦{amount} successfully.")

    def main_menu(self):
        while True:
            print("\nPlease select an option:")
            print("1. Sign up")
            print("2. Login")
            print("3. Exit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                self.signup()
            elif choice == '2':
                self.login()
            elif choice == '3':
                Repository.save_all(self.users, self.wallets)
                self.exit_program()
            else:
                print("Invalid choice. Please select a valid option.")

    def exit_program(self):
        print("Exiting the program.")
        exit()


if __name__ == "__main__":
    app = WalletApp()
    app.main_menu()
