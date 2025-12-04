"""This module defines the Account Details window."""

__author__ = "ACE Faculty"
__version__ = "4.01.2025"
__credits__ = "Elijah Juayang"

from ui_superclasses.details_window import DetailsWindow
from bank_account.bank_account import BankAccount
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
import copy

class AccountDetailsWindow(DetailsWindow):
    """A class used to display account details and perform bank account 
    transactions.
    """

    balance_updated = Signal(BankAccount)
    """A bank account containing an updated balance."""

    def __init__(self, account: BankAccount):
        """Initializes a new instance of the ExtendedAccountDetails 
        window.

        Args:
            account (BankAccount): The bank account to be modified.
        """

        super().__init__()

        if not isinstance(account, BankAccount):
            self.reject()

        self.__account = copy.deepcopy(account)

        self.account_number_label.setText(str(self.__account.account_number))
        self.balance_label.setText(f"${self.__account.balance:,.2f}")

        self.deposit_button.clicked.connect(self.__on_apply_transaction)
        self.withdraw_button.clicked.connect(self.__on_apply_transaction)
        self.exit_button.clicked.connect(self.__on_exit)
            
    @Slot()
    def __on_apply_transaction(self):
        """Performs a transaction to the bank account using the 
        amount entered.
        """

        transaction_amount = self.transaction_amount_edit.text()

        try:
            transaction_amount = float(transaction_amount)
        except ValueError:
            QMessageBox.information(
                self, "Invalid Data", "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return
        
        try:
            if self.sender() == self.deposit_button:
                transaction = "Deposit"
                self.__account.deposit(transaction_amount)

            elif self.sender() == self.withdraw_button:
                transaction = "Withdraw"
                self.__account.withdraw(transaction_amount)
            
            self.balance_label.setText(f"${self.__account.balance:,.2f}")

        except ValueError as e:
            QMessageBox.information(self, f"{transaction} Failed", e)

        self.transaction_amount_edit.setText("")
        self.transaction_amount_edit.setFocus()
        self.balance_updated.emit(self.__account)

    @Slot()
    def __on_exit(self):
        """Closes the account details window."""

        self.close()
