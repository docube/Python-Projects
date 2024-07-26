# repo.py class file - Repository Class

# Import functions, classes and Libraries defined within class and from other class files
import csv
import os
import random
from model import User, Wallet, Transaction

# File paths for CSV files
users_file = 'users.csv'
wallets_file = 'wallets.csv'
transactions_file = 'transactions.csv'

class UserRepository:
    users = {}

    @staticmethod
    def load_data():
        if os.path.exists(users_file):
            with open(users_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    username, password, wallet_id, first_name, middle_name, last_name = row
                    user = User(username, password, wallet_id, first_name, middle_name, last_name)
                    UserRepository.users[username] = user

    @staticmethod
    def save_data():
        with open(users_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for user in UserRepository.users.values():
                writer.writerow([user.username, user.password, user.wallet.wallet_id, user.first_name, user.middle_name, user.last_name])

    @staticmethod
    def create_user(username, password, first_name, middle_name, last_name):
        wallet_id = UserRepository.generate_wallet_id()
        user = User(username, password, wallet_id, first_name, middle_name, last_name)
        UserRepository.users[username] = user
        WalletRepository.wallets[username] = user.wallet

    @staticmethod
    def generate_wallet_id():
        return str(random.randint(1000000000, 9999999999))

class WalletRepository:
    wallets = {}

    @staticmethod
    def load_data():
        if os.path.exists(wallets_file):
            with open(wallets_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    username, wallet_id, balance = row
                    wallet = Wallet(username, wallet_id, float(balance))
                    WalletRepository.wallets[username] = wallet

    @staticmethod
    def save_data():
        with open(wallets_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for wallet in WalletRepository.wallets.values():
                writer.writerow([wallet.username, wallet.wallet_id, wallet.balance])

class TransactionRepository:
    transactions = []

    @staticmethod
    def load_data():
        if os.path.exists(transactions_file):
            with open(transactions_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    username, txn_id, txn_details = row
                    user = UserRepository.users[username]
                    txn = Transaction.from_string(txn_details, int(txn_id))
                    user.add_transaction(txn)
                    TransactionRepository.transactions.append(txn)
                    if Transaction.id_counter <= txn.id:
                        Transaction.id_counter = txn.id + 1

    @staticmethod
    def save_data():
        with open(transactions_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for user in UserRepository.users.values():
                for txn in user.transactions:
                    writer.writerow([user.username, txn.id, txn.details()])
