# model.py
import csv
import os

users_file = 'users.csv'
wallets_file = 'wallets.csv'
transactions_file = 'transactions.csv'


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.wallet = Wallet(username)
        self.transactions = []


class Wallet:
    def __init__(self, username, balance=400.0):
        self.username = username
        self.balance = balance


class Transaction:
    id_counter = 1

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
