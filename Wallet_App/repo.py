# repo.py
import csv
import os
import random
from model import User, Wallet, Transaction
from config import users_file, wallets_file, transactions_file

class UserRepository:
    users = {}

    @staticmethod
    def load_data():
        if os.path.exists(users_file):
            with open(users_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 6:
                        username, password, wallet_id, first_name, middle_name, last_name = row
                        UserRepository.users[username] = User(username, password, wallet_id, first_name, middle_name, last_name)
                    else:
                        raise ValueError(f"Unexpected row format: {row}")

    @staticmethod
    def save_data():
        with open(users_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for user in UserRepository.users.values():
                writer.writerow([user.username, user.password, user.wallet_id, user.first_name, user.middle_name, user.last_name])

class WalletRepository:
    wallets = {}

    @staticmethod
    def load_data():
        if os.path.exists(wallets_file):
            with open(wallets_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 3:
                        username, balance, wallet_id = row
                        WalletRepository.wallets[username] = Wallet(username, wallet_id, float(balance))
                    else:
                        raise ValueError(f"Unexpected row format: {row}")

    @staticmethod
    def save_data():
        with open(wallets_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for wallet in WalletRepository.wallets.values():
                writer.writerow([wallet.username, wallet.balance, wallet.wallet_id])

class TransactionRepository:
    @staticmethod
    def load_data():
        if os.path.exists(transactions_file):
            with open(transactions_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 3:
                        username, txn_id, txn_details = row
                        user = UserRepository.users[username]
                        txn = TransactionRepository.from_string(txn_details, int(txn_id))
                        user.transactions.append(txn)
                        if Transaction.id_counter <= txn.id:
                            Transaction.id_counter = txn.id + 1
                    else:
                        raise ValueError(f"Unexpected row format: {row}")

    @staticmethod
    def save_data():
        with open(transactions_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for user in UserRepository.users.values():
                for txn in user.transactions:
                    writer.writerow([user.username, txn.id, txn.details()])

    @staticmethod
    def from_string(details, txn_id):
        parts = details.split()
        amount = float(parts[1][1:])
        if parts[0] == "Deposited":
            return Transaction(parts[0], parts[0], amount, deposit=True)
        return Transaction(parts[2], parts[-1], amount)
