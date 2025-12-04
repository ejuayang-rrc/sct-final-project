"""This module defines the ManagementFeeStrategy class."""

__version__ = "3.08.2025"
__credits__ = "Elijah Juayang"

from datetime import date, timedelta
from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):
    """A class representing a management fee strategy."""

    def __init__(self, date_created: date, management_fee: float):
        """Initializes an instance of the ManagementFeeStrategy class.
        
        Args:
            date_created (date): The date the account was created.
            management_fee (float): A flat-rate fee the bank charges for
                managing an account.
        """

        self.__date_created = date_created 
        self.__management_fee = management_fee
        self.TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates the service charge cost of a client's 
        bank account. 
        
        Args:
            account (BankAccount): The client's bank account.

        Returns:
            float: The calculated service charge of the bank account.
        """

        service_charge = self.BASE_SERVICE_CHARGE

        # Compares if a date from 10 years ago is before date created.
        if self.TEN_YEARS_AGO <= self.__date_created:
            service_charge += self.__management_fee

        return service_charge
