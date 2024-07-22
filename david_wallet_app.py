import csv
import os

# File paths for CSV files
users_file = 'users.csv'
wallets_file = 'wallets.csv'
transactions_file = 'transactions.csv'

# Dictionary to store user data (for authentication)
users = {}

# Dictionary to store wallet data
wallets = {}

# Dictionary to store transactions
transactions = {}

def load_data():
    # Load users data
    if os.path.exists(users_file):
        with open(users_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                users[row[0]] = row[1]

    # Load wallets data
    if os.path.exists(wallets_file):
        with open(wallets_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                wallets[row[0]] = float(row[1])

    # Load transactions data
    if os.path.exists(transactions_file):
        with open(transactions_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                username = row[0]
                txn_id = int(row[1])
                txn_details = row[2]
                if username not in transactions:
                    transactions[username] = []
                transactions[username].append((txn_id, txn_details))

def save_data():
    # Save users data
    with open(users_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for username, password in users.items():
            writer.writerow([username, password])

    # Save wallets data
    with open(wallets_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for username, balance in wallets.items():
            writer.writerow([username, balance])

    # Save transactions data
    with open(transactions_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for username, txns in transactions.items():
            for txn in txns:
                writer.writerow([username, txn[0], txn[1]])

def signup():
    print("Sign Up")
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Please try a different one.")
        return
    
    password = input("Enter a password: ")
    users[username] = password
    wallets[username] = 400.0  # Initialize wallet balance to 0
    transactions[username] = []  # Initialize empty transaction list
    print("Sign up successful! Logging you in...")

    # Call login function immediately after sign up
    login(username, password)

def login(username=None, password=None):
    print("Log In")

    if username is None:
        username = input("Enter your username: ")

    if password is None:
        password = input("Enter your password: ")

    if username not in users:
        print("Username not found. Please sign up first.")
        return

    if users[username] == password:
        print("Login successful!")
        dashboard(username)  # Call the wallet function after successful login
    else:
        print("Incorrect password. Please try again.")

def dashboard(username):
    print(f"Welcome to your wallet, {username}!")

    while True:
        print("\nPlease select an option:")
        print("1. Send money")
        print("2. View balance")
        print("3. View transactions")
        print("4. Logout")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            send_money(username)
        elif choice == '2':
            view_balance(username)
        elif choice == '3':
            view_transactions(username)
        elif choice == '4':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def send_money(sender):
    recipient = input("Enter the recipient's username: ")
    if recipient not in users:
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

    if wallets[sender] < amount:
        print("Insufficient balance.")
        return

    wallets[sender] -= amount
    wallets[recipient] += amount

    transaction_id = len(transactions[sender]) + 1
    transactions[sender].append((transaction_id, f"Sent {amount} to {recipient}"))
    transactions[recipient].append((transaction_id, f"Received {amount} from {sender}"))

    print(f"Sent ₦{amount} to {recipient} successfully.")

def view_balance(username):
    print(f"Your current balance is: ₦{wallets[username]}")

def view_transactions(username):
    if not transactions[username]:
        print("No transactions found.")
        return

    print("Your transactions:")
    for txn in transactions[username]:
        print(f"{txn[0]}. {txn[1]}")

    try:
        txn_id = int(input("Enter the transaction ID to view details or 0 to return: "))
        if txn_id == 0:
            return
        txn = next((t for t in transactions[username] if t[0] == txn_id), None)
        if txn:
            print(f"Transaction {txn_id}: {txn[1]}")
        else:
            print("Transaction ID not found.")
    except ValueError:
        print("Invalid input.")

def exit_program():
    print("Exiting the program.")
    exit()

def main_menu():
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
            exit_program()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()