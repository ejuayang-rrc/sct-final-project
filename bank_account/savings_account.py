"""This module defines a class representing a Savings Account."""

__author__ = "Elijah Juayang"
__version__ = "3.10.2025"

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """A class that represents a client's savings account."""

    #region -------------- Initializing Object --------------

    def __init__(self, account_number: int, client_number: int, 
                 balance: float, date_created: date, minimum_balance: float):
        """Initializes an instance of the SavingsAccount class.
        
        Args:
            account_number (int): The account number of the 
                Savings Account.
            client_number (int): The client number of the Savings 
                Account.
            balance (float): The current balance of the Savings Account.
            date_created (date): The date the account was created.
            minimum_balance (float): The minimum value balance can be
                before further service charges are applied.

        Raises:
            ValueError: If account number or client number is not
                an integer value.
        """

        # Superclass BankAccount
        super().__init__(account_number, client_number, balance, date_created)

        # Try-Except to verify if management_fee can convert to float.
        try:
            minimum_balance = float(minimum_balance)
        except ValueError:
            minimum_balance = 50.0

        self.__minimum_balance = minimum_balance
        self.__strategy = MinimumBalanceStrategy(minimum_balance)

    #region -------------- String Method -------------- 

    def __str__(self) -> str:
        """Creates a formatted message detailing the Savings Account's 
        values and details.
        
        Returns:
            str: A string displaying the Savings Account's details.
        """

        # Variable to shorten return line.
        minimum_balance = self.__minimum_balance

        return super().__str__() + \
            f"Minimum Balance: ${minimum_balance:,.2f} Account Type: Savings"

    #region -------------- Methods --------------

    def get_service_charges(self) -> float:
        """Returns the calculated service charge the Savings Account will
        incur.

        Returns:
            float: The calculated service charge of the Savings Account.
        """

        return self.__strategy.calculate_service_charges(self)
        