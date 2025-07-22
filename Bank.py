# Create a BankAccount class that has:

# Properties: account_holder, balance (starts at 0)
# Methods: deposit(), withdraw() (check if sufficient funds), check_balance(), transfer_to() another account


#A simple BankAccount class implementation

def validate_amount(amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    return amount

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        validate_amount(amount)
        self.balance += amount

    def withdraw(self, amount):
        validate_amount(amount)
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def check_balance(self):
        return self.balance

    def transfer_to(self, other_account, amount):
        validate_amount(amount)
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        other_account.deposit(amount)

BankAccountHolder = BankAccount("Emmanuel AAkomdo")
BankAccountHolder.deposit(1000)
print(f"Balance after deposit: {BankAccountHolder.check_balance()}")
BankAccountHolder.withdraw(200)
print(f"Balance after withdrawal: {BankAccountHolder.check_balance()}")
another_account = BankAccount("Kwesi Mensah")
BankAccountHolder.transfer_to(another_account, 300)
print(f"Balance after transfer: {BankAccountHolder.check_balance()}")
print(f"Kwesi Mensah's balance after transfer: {another_account.check_balance()}")
print(f"Account Holder: {BankAccountHolder.account_holder}")
print(f"Another Account Holder: {another_account.account_holder}")
print(f"Final Balance of {BankAccountHolder.account_holder}: {BankAccountHolder.check_balance()}")
print(f"Final Balance of {another_account.account_holder}: {another_account.check_balance()}")
print("Bank operations completed successfully.")


