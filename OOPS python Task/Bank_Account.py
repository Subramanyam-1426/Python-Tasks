class Bank_Account:
    # Stores the bank name shared by all accounts.
    bank_name = "State Bank of India"

    # Keeps track of the total number of accounts created.
    total_accounts = 0

    # Defines the minimum balance that must be maintained.
    MIN_BALANCE = 500

    # Stores the next account number to be assigned.
    _next_account_number = 1001

    # Stores the annual interest rate for all accounts.
    interest_rate = 4.0

    # Initializes a new bank account with holder details, deposit, and PIN.
    def __init__(self, holder_name, account_type, initial_deposit, pin):
        self.holder_name = holder_name
        self.account_type = account_type
        self.__balance = 0
        self.initial_deposit = initial_deposit
        self.__pin = pin

        self._next_account_number += 1
        Bank_Account.total_accounts += 1

    # Returns the initial deposited amount (current balance).
    @property
    def initial_deposit(self):
        return self.__balance

    # Returns the account number of the account.
    @property
    def account_number(self):
        return self._next_account_number

    # Returns the current account balance.
    @property
    def balance(self):
        return self.__balance

    # Validates and sets the initial deposit amount.
    @initial_deposit.setter
    def initial_deposit(self, amount):
        if (not isinstance(amount, (int, float))):
            raise TypeError(f"Amount should be in integer or float")
        if amount < Bank_Account.MIN_BALANCE:
            raise ValueError("Minimum amount should be 500")
        self.__balance = amount

    # Deposits a valid amount into the account and updates the balance.
    def deposit(self, amount):
        if (not isinstance(amount, (int, float))):
            raise TypeError(f"Amount should be in integer or float")
        if amount < 0:
            raise ValueError("Amount ahould be positive")
        self.__balance += amount
        return self.balance

    # Withdraws money after verifying the PIN and ensuring the minimum balance is maintained.
    def withdraw(self, amount, pin):
        if (pin == self.__pin):
            if (not isinstance(amount, (int, float))):
                raise TypeError(f"Amount should be in integer or float")
            if amount > self.__balance - 500:
                raise ValueError(
                    "Blocked (below min) Insufficient funds,Minimum balance 500 must remain")
            self.__balance -= amount
            return self.balance
        else:
            print("Check your pin number")

    # Verifies whether the entered PIN is correct.
    def __verify_pin(self, pin):
        if not self.__pin == pin:
            print(f"Blocked (wrong PIN): Incorrect PIN")
        return self.__pin == pin

    # Changes the account PIN after validating the old PIN.
    def change_pin(self, oldpin, newpin):
        if (oldpin == self.__pin):
            self.__pin = newpin
            print("PIN CHANGED SUCCESSFULLY")
        else:
            print("Check your old pin once")

    # Adds annual interest to the current account balance.
    def add_annual_interest(self):
        temp = self.balance
        self.__balance += temp * Bank_Account.interest_rate * 0.01
        return self.balance

    # Returns the total number of bank accounts created.
    def get_total_accounts():
        return Bank_Account.total_accounts

    # Checks whether the given amount is a valid positive value.
    @staticmethod
    def is_valid_amount(value):
        return value > 0

    # Returns a readable string representation of the bank account.
    def __str__(self):
        return (
            f"Accpunt [{self.account_number}] | {self.holder_name} | {self.account_type} | "
            f" Rs.{self.balance}"
        )


# Creates sample bank accounts and demonstrates different banking operations.
def main():
    print(f"Bank: {Bank_Account.bank_name}")
    try:
        b1 = Bank_Account("Varun Kumar", "Savings", 5000.0, 9912)
        b2 = Bank_Account("Subbu", "Savings", 20000.0, 1123)

        print(b1)
        print(b2)
        print(f"Total accounts: {Bank_Account.get_total_accounts()}")
        print(f"Deposit 2000 -> {b1.deposit(2000)}")
        print(f"Withdraw 1500 -> {b1.withdraw(1500, 9912)}")
        print(f"Interest added: {b1.add_annual_interest()}")

        print(f"Balance now: {b1.balance}")
        b1.change_pin(9912, 1234)
        b1.change_pin(4358, 1234)
    except (ValueError, TypeError) as error:
        print(error)

    try:
        b3 = Bank_Account("Ramesh", "Savings", 400, 1234)
    except (ValueError, TypeError) as error:
        print(f"Blocked : {error}")

    try:
        b4 = Bank_Account("Ramesh", "Savings", 4000, 1234)
        b4.withdraw(4000, 1234)
    except (ValueError, TypeError) as error:
        print(f"Blocked : {error}")

    try:
        b5 = Bank_Account("Ramesh", "Savings", 4000, 1234)
        b5.withdraw(3000, 1235)
    except (ValueError, TypeError) as error:
        print(f"Blocked : {error}")

    try:
        b1.balance = 1000
    except (AttributeError) as error:
        print(f"Blocked : {error}")


# Executes the program when this file is run directly.
if __name__ == "__main__":
    main()