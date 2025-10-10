class ValueTooLowError(Exception):
    """Raised when the deposit amount is not positive."""
    pass

class BankAccount:
    """A simple bank account class."""
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueTooLowError("Deposit amount must be greater than zero.")

        self.account_balance += amount
        print(f"Deposited: ${amount}")
        return self.account_balance
    
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Return the current account balance."""
        print(f"Current Balance: ${self.account_balance}")
        return float(self.account_balance)