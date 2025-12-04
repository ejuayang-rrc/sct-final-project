"""This module defines the ServiceChargeStrategy class."""

__author__ = "Elijah Juayang"
__version__ = "3.08.2025"

from abc import ABC, abstractmethod
from bank_account.bank_account import BankAccount

class ServiceChargeStrategy(ABC):
    """A class representing a general strategy for calculating service 
    charge.
    """

    BASE_SERVICE_CHARGE = 0.5
    """The base service charge."""

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount) -> float:
        """Calculates the service charge cost of a client's 
        bank account. 
        
        Args:
            account (BankAccount): The client's bank account.

        Returns:
            float: The calculated service charge of the bank account.
        """

        pass
