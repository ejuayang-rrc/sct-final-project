"""This module defines the OverdraftStrategy class."""

__version__ = "3.08.2025"
__credits__ = "Elijah Juayang"

from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """A class representing an overdraft strategy."""

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """Initializes an instance of the OverdraftStrategy class.

        Args:
            overdraft_limit (float): The maximum amount a balance can be 
                overdrawn before overdraft fees are applies.
            overdraft_rate (float): The rate to which overdraft fees are 
                applied.
        """

        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates the service charge cost of a client's 
        bank account. 
        
        Args:
            account (BankAccount): The client's bank account.

        Returns:
            float: The calculated service charge of the bank account.
        """

        # Pre-made value to be unchanged if balance is over limit.
        service_charge = self.BASE_SERVICE_CHARGE

        # Updates service_charge if balance is under overdraft limit.
        if account.balance < self.__overdraft_limit:
            service_charge = self.BASE_SERVICE_CHARGE + \
                (self.__overdraft_limit - account.balance) * \
                    self.__overdraft_rate
            
        return service_charge
