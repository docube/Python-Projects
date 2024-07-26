import csv
import os
import random

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
                    username, password, wallet_id, first_name, middle_name, last_name = row
                    User.users[username] = User(username, password, wallet_id, first_name, middle_name, last_name)

    @staticmethod
    def save_data():
        with open(users_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for user in User.users.values():
                writer.writerow([user.username, user.password, user.wallet.wallet_id, user.first_name, user.middle_name, user.last_name])

    def __init__(self, username, password, wallet_id=None, first_name=None, middle_name=None, last_name=None):
        self.username = username
        self.password = password
        self.wallet = Wallet(username, wallet_id)
        self.transactions = []
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

class Wallet:
    wallets = {}

    @staticmethod
    def load_data():
        if os.path.exists(wallets_file):
            with open(wallets_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    username, balance, wallet_id = row
                    Wallet.wallets[wallet_id] = Wallet(username, float(balance), wallet_id)

    @staticmethod
    def save_data():
        with open(wallets_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for wallet in Wallet.wallets.values():
                writer.writerow([wallet.username, wallet.balance, wallet.wallet_id])

    def __init__(self, username, balance=400.0, wallet_id=None):
        self.username = username
        self.balance = balance
        self.wallet_id = wallet_id if wallet_id else self.generate_wallet_id()
        Wallet.wallets[self.wallet_id] = self

    @staticmethod
    def generate_wallet_id():
        while True:
            wallet_id = str(random.randint(1000000000, 9999999999))
            if wallet_id not in Wallet.wallets:
                return wallet_id

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
