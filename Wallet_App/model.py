# model.py
import random

class User:
    def __init__(self, username, password, wallet_id, first_name, middle_name, last_name):
        self.username = username
        self.password = password
        self.wallet_id = wallet_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.wallet = Wallet(username, wallet_id)
        self.transactions = []

class Wallet:
    def __init__(self, username, wallet_id, balance=400.0):
        self.username = username
        self.wallet_id = wallet_id
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
