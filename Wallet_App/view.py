from repo import UserRepo, WalletRepo

def main_menu():
    User.load_data()
    Wallet.load_data()
    Transaction.load_data()

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
            User.save_data()
            Wallet.save_data()
            Transaction.save_data()
            exit_program()
        else:
            print("Invalid choice. Please select a valid option.")

def signup():
    print("Sign Up")
    username = input("Enter a username: ")
    first_name = input("Enter your first name: ")
    middle_name = input("Enter your middle name: ")
    last_name = input("Enter your last name: ")
    password = input("Enter a password: ")

    user = UserRepo.create_user(username, password, first_name, middle_name, last_name)
    if user:
        print("Sign up successful! Logging you in...")
        login(username, password)
    else:
        print("Username already exists. Please try a different one.")

def login(username=None, password=None):
    print("Log In")

    if username is None:
        username = input("Enter your username: ")

    if password is None:
        password = input("Enter your password: ")

    user = UserRepo.get_user(username)
    if user and user.password == password:
        print("Login successful!")
        dashboard(user)  # Call the wallet function after successful login
    else:
        print("Incorrect username or password. Please try again.")

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
    amount = float(input("Enter the amount to send: ₦"))
    if WalletRepo.send_money(user.username, recipient_username, amount):
        print(f"Sent ₦{amount} to {recipient_username} successfully.")
    else:
        print("Transfer failed. Check recipient username and your balance.")

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
    amount = float(input("Enter the amount to deposit: ₦"))
    if WalletRepo.deposit_money(user.username, amount):
        print(f"Deposited ₦{amount} successfully.")
    else:
        print("Deposit failed.")

def exit_program():
    print("Exiting the program.")
    exit()

if __name__ == "__main__":
    main_menu()
