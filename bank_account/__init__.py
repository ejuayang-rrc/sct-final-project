"""An import for the BankAccount class and it's subclasses."""

__author__ = "Elijah Juayang"
__version__ = "2.12.2025"

# Superclass
from .bank_account import BankAccount

# BankAccount Subclasses
from .chequing_account import ChequingAccount
from .investment_account import InvestmentAccount
from .savings_account import SavingsAccount

__all__ = [
    "BankAccount", 
    "ChequingAccount", 
    "InvestmentAccount", 
    "SavingsAccount"
]
