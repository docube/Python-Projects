# view.py
from model import User, Wallet, Transaction
from repo import UserRepository, WalletRepository, TransactionRepository

def signup():
    print("Sign Up")
    username = input("Enter a username: ")
    if username in UserRepository.users:
        print("Username already exists. Please try a different one.")
        return

    password = input("Enter a password: ")
    first_name = input("Enter your first name: ")
    middle_name = input("Enter your middle name: ")
    last_name = input("Enter your last name: ")

    UserRepository.create_user(username, password, first_name, middle_name, last_name)
    print("Sign up successful! Logging you in...")

    login(username, password)

def login(username=None, password=None):
    print("Log In")

    if username is None:
        username = input("Enter your username: ")

    if password is None:
        password = input("Enter your password: ")

    if username not in UserRepository.users:
        print("Username not found. Please sign up first.")
        return

    user = UserRepository.users[username]
    if user.password == password:
        print("Login successful!")
        dashboard(user)
    else:
        print("Incorrect password. Please try again.")

def dashboard(user):
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
            send_money(user)
        elif choice == '2':
            view_balance(user)
        elif choice == '3':
            view_transactions(user)
        elif choice == '4':
            deposit_money(user)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def send_money(user):
    recipient_username = input("Enter the recipient's username: ")
    if recipient_username not in UserRepository.users:
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

    if user.wallet.balance < amount:
        print("Insufficient balance.")
        return

    recipient = UserRepository.users[recipient_username]
    user.wallet.balance -= amount
    recipient.wallet.balance += amount

    transaction = Transaction(user.username, recipient_username, amount)
    user.add_transaction(transaction)
    recipient.add_transaction(transaction)

    print(f"Sent ₦{amount} to {recipient_username} successfully.")

def view_balance(user):
    print(f"Your current balance is: ₦{user.wallet.balance}")

def view_transactions(user):
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

def deposit_money(user):
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
    user.add_transaction(transaction)
    print(f"Deposited ₦{amount} successfully.")

def main_menu():
    UserRepository.load_data()
    WalletRepository.load_data()
    TransactionRepository.load_data()

    while True:
        print("\nPlease select an option:")
        print("1. Sign up")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            UserRepository.save_data()
            WalletRepository.save_data()
            TransactionRepository.save_data()
            exit_program()
        else:
            print("Invalid choice. Please select a valid option.")

def exit_program():
    print("Exiting the program.")
    exit()

if __name__ == "__main__":
    main_menu()
