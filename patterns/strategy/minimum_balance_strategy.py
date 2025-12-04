"""This module defines the MinimumBalanceStrategy class."""

__version__ = "3.08.2025"
__credits__ = "Elijah Juayang"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """A class representing a minimum balance strategy."""

    def __init__(self, minimum_balance: float):
        """Initializes an instance of the MinimumBalanceStrategy class.
        
        Args:
            minimum_balance (float): The minimum value balance can be
                before further service charges are applied.
        """

        self.__minimum_balance = minimum_balance
        self.SERVICE_CHARGE_PREMIUM = 2.0

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates the service charge cost of a client's 
        bank account. 
        
        Args:
            account (BankAccount): The client's bank account.

        Returns:
            float: The calculated service charge of the bank account.
        """

        # Value is unchanged if balance is over/equal minimum balance.
        service_charge = self.BASE_SERVICE_CHARGE

        # Updates service_charge if balance is under minimum balance.
        if account.balance < self.__minimum_balance:
            service_charge *= self.SERVICE_CHARGE_PREMIUM

        return service_charge
    