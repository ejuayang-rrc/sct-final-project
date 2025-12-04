"""This module defines a class representing an Investment Account."""

__author__ = "Elijah Juayang"
__version__ = "3.10.2025"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    """A class that represents a client's investment account."""

    #region -------------- Initializing Object --------------

    def __init__(self, account_number: int, client_number: int, balance: float, 
                 date_created: date, management_fee: float):
        """Initializes an instance of the InvestmentAccount class.
        
        Args:
            account_number (int): The account number of the 
                Investment Account.
            client_number (int): The client number of the Investment 
                Account.
            balance (float): The current balance of the Investment 
                Account.
            date_created (date): The date the account was created.
            management_fee (float): A flat-rate fee the bank charges for
                managing an account.

        Raises:
            ValueError: If account number or client number is not
                an integer value.
        """

        # Superclass BankAccount
        super().__init__(account_number, client_number, balance, date_created)

        # Try-Except to verify if management_fee can convert to float.
        try:
            management_fee = float(management_fee)
        except ValueError:
            management_fee = 2.55

        # Gets date from 10 years ago by subtracting 10 years off today.
        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

        # Private Attribute
        self.__management_fee = management_fee
        self.__strategy = ManagementFeeStrategy(date_created, management_fee)

    #region -------------- String Method -------------- 

    def __str__(self) -> str:
        """Creates a formatted message detailing the Investment 
        Account's status and details.
        
        Returns:
            str: A string displaying the Investment Account's details.
        """

        management_fee = f"${self.__management_fee:,.2f}"

        # Compares if a date from 10 years ago is before date created.
        if self.TEN_YEARS_AGO > self._date_created:
            management_fee = "Waived"
        
        # Variable to shorten return line.
        account_details = (f"Date Created: {self._date_created} "
                           f"Management Fee: {management_fee} "
                           "Account Type: Investment")

        return super().__str__() + account_details

    #region -------------- Method --------------

    def get_service_charges(self) -> float:
        """Returns the calculated service charge the Investment Account 
        will incur.

        Returns:
            float: The calculated service charge of the Investment 
                Account.
        """

        return self.__strategy.calculate_service_charges(self)
