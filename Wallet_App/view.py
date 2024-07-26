# view.py
import random
from repo import UserRepository, WalletRepository, TransactionRepository
from model import User, Wallet, Transaction

def main_menu():
    UserRepository.load_data()
    WalletRepository.load_data()
    TransactionRepository.load_data()

    while True:
        print("\nPlease select an option:")
        print("1. Sign up")
        print("2. Login")
        print("3. Deposit")
        print("4. Transfer")
        print("5. View Balance")
        print("6. View Transactions")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            signup()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Please Login into your wallet.")
        elif choice == '4':
            print("Please Login into your wallet.")
        elif choice == '5':
            print("Please Login into your wallet.")
        elif choice == '6':
            print("Please Login into your wallet.")
        elif choice == '7':
            UserRepository.save_data()
            WalletRepository.save_data()
            TransactionRepository.save_data()
            exit_program()
        else:
            print("Invalid choice. Please select a valid option.")

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
    wallet_id = generate_wallet_id()

    user = User(username, password, wallet_id, first_name, middle_name, last_name)
    UserRepository.users[username] = user
    UserRepository.save_data()
    WalletRepository.save_data()
    print("Sign up successful! Logging you in...")

    # Call login function immediately after sign up
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
        dashboard(user)  # Call the wallet function after successful login
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
            user.wallet.send_money()
        elif choice == '2':
            user.wallet.view_balance()
        elif choice == '3':
            user.wallet.view_transactions()
        elif choice == '4':
            user.wallet.deposit_money()
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def generate_wallet_id():
    return str(random.randint(1000000000, 9999999999))

def exit_program():
    print("Exiting the program.")
    exit()

if __name__ == "__main__":
    main_menu()
