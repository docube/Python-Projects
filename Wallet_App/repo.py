from model import User, Wallet, Transaction

class UserRepo:

    @staticmethod
    def create_user(username, password, first_name, middle_name, last_name):
        if username in User.users:
            return None
        user = User(username, password, first_name=first_name, middle_name=middle_name, last_name=last_name)
        User.users[username] = user
        Wallet.save_data()
        User.save_data()
        return user

    @staticmethod
    def get_user(username):
        return User.users.get(username)

class WalletRepo:

    @staticmethod
    def send_money(sender_username, recipient_username, amount):
        sender = UserRepo.get_user(sender_username)
        recipient = UserRepo.get_user(recipient_username)
        if sender and recipient and sender.wallet.balance >= amount:
            sender.wallet.balance -= amount
            recipient.wallet.balance += amount
            transaction = Transaction(sender.username, recipient.username, amount)
            sender.add_transaction(transaction)
            recipient.add_transaction(transaction)
            Wallet.save_data()
            Transaction.save_data()
            return True
        return False

    @staticmethod
    def deposit_money(username, amount):
        user = UserRepo.get_user(username)
        if user:
            user.wallet.balance += amount
            transaction = Transaction(user.username, user.username, amount, deposit=True)
            user.add_transaction(transaction)
            Wallet.save_data()
            Transaction.save_data()
            return True
        return False

class TransactionRepo:
    pass  # For now, all transaction-related functions are handled within User and Wallet classes
