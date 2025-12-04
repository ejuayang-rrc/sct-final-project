"""This module defines a class representing a Chequing Account."""

__author__ = "Elijah Juayang"
__version__ = "3.10.2025"

from datetime import date
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """A class that represents a client's chequing account."""
    
    #region -------------- Initializing Object --------------

    def __init__(self, account_number: int, client_number: int, balance: float, 
                 date_created: date, overdraft_limit: float, 
                 overdraft_rate: float):
        """Initializes an instance of the ChequingAccount class.
        
        Args:
            account_number (int): The account number of the 
                Chequing Account.
            client_number (int): The client number of the 
                Chequing Account.
            balance (float): The current balance of the 
                Chequing Account.
            date_created (date): The date the account was created.
            overdraft_limit (float): The maximum amount a balance can be 
                overdrawn before overdraft fees are applies.
            overdraft_rate (float): The rate to which overdraft fees are 
                applied.

        Raises:
            ValueError: If account number or client number is not
                an integer value.
        """

        # Superclass BankAccount
        super().__init__(account_number, client_number, balance, date_created)

        # Try-Except blocks used for float conversion Validation.
        try:
            overdraft_limit = float(overdraft_limit)
        except ValueError:
            overdraft_limit = -100.0

        try:
            overdraft_rate = float(overdraft_rate)
        except ValueError:
            overdraft_rate = 0.05

        # Private Attributes
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate
        self.__strategy = OverdraftStrategy(overdraft_limit, overdraft_rate)

    #region -------------- String Method -------------- 

    def __str__(self) -> str:
        """Creates a formatted message detailing the Chequing Account's 
        values and details.
        
        Returns:
            str: A string displaying the Chequing Account's details.
        """

        # Variables to make string variable below under 80 characters.
        overdraft_limit = self.__overdraft_limit
        overdraft_rate = self.__overdraft_rate

        account_details = (f"Overdraft Limit: ${overdraft_limit:,.2f} "
                           f"Overdraft Rate: {overdraft_rate * 100:,.2f}% "
                           "Account Type: Chequing")

        return super().__str__() + account_details
    
    #region -------------- Methods --------------

    def get_service_charges(self) -> float:
        """Returns the calculated service charge the Chequing Account 
        will incur.

        Returns:
            float: The calculated service charge of the Chequing 
                Account.
        """

        return self.__strategy.calculate_service_charges(self)
