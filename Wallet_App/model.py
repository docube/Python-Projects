# model.py

class User:
    def __init__(self, username, password, wallet_id, first_name, middle_name, last_name):
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

    @staticmethod
    def from_string(details, txn_id):
        parts = details.split()
        amount = float(parts[1][1:])
        if parts[0] == "Deposited":
            return Transaction(parts[0], parts[0], amount, deposit=True)
        return Transaction(parts[2], parts[-1], amount)
