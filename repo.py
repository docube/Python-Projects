# repo.py
import csv
import os
from model import User, Wallet, Transaction

users_file = 'users.csv'
wallets_file = 'wallets.csv'
transactions_file = 'transactions.csv'


class Repository:
    @staticmethod
    def load_users():
        users = {}
        if os.path.exists(users_file):
            with open(users_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    username, password = row
                    users[username] = User(username, password)
        return users

    @staticmethod
    def save_users(users):
        with open(users_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for user in users.values():
                writer.writerow([user.username, user.password])

    @staticmethod
    def load_wallets():
        wallets = {}
        if os.path.exists(wallets_file):
            with open(wallets_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    username, balance = row
                    wallets[username] = Wallet(username, float(balance))
        return wallets

    @staticmethod
    def save_wallets(wallets):
        with open(wallets_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for wallet in wallets.values():
                writer.writerow([wallet.username, wallet.balance])

    @staticmethod
    def load_transactions(users):
        if os.path.exists(transactions_file):
            with open(transactions_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    username, txn_id, txn_details = row
                    user = users[username]
                    txn = Transaction.from_string(txn_details, int(txn_id))
                    user.transactions.append(txn)
                    if Transaction.id_counter <= txn.id:
                        Transaction.id_counter = txn.id + 1

    @staticmethod
    def save_transactions(users):
        with open(transactions_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for user in users.values():
                for txn in user.transactions:
                    writer.writerow([user.username, txn.id, txn.details()])

    @staticmethod
    def save_all(users, wallets):
        Repository.save_users(users)
        Repository.save_wallets(wallets)
        Repository.save_transactions(users)
