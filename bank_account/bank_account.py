"""This module defines a class representing a client's Bank Account."""

__author__ = "Elijah Juayang"
__version__ = "3.10.2025"

from abc import ABC, abstractmethod
from datetime import date
from patterns.observer.subject import Subject
from patterns.observer.observer import Observer

class BankAccount(Subject, ABC):
    """A class representing a client's bank account."""

    #region -------------- Initializing Object --------------

    @abstractmethod
    def __init__(self, account_number: int, client_number: int, 
                 balance: float, date_created: date):
        """Initializes an instance of the BankAccount class.
        
        Args:
            account_number (int): The account number of the 
                Bank Account.
            client_number (int): The client number of the Bank Account.
            balance (float): The current balance of the Bank Account.
            date_created (date): The date the account was created.

        Raises:
            ValueError: If account number or client number is not
                an integer value.
        """

        # This is not needed but instructions ask for it.
        super().__init__()

        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        
        # Try except used if amount value can't convert to float.
        try:
            balance = float(balance)
        except ValueError:
            balance = 0

        if not isinstance(date_created, date):
            date_created = date.today()

        # Constant Attributes
        self.LARGE_TRANSACTION_THRESHOLD = 9999.99
        self.LOW_BALANCE_LEVEL = 50.0

        # Private Attributes
        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = balance

        # Protected Attribute
        self._date_created = date_created

    #region -------------- Accessors --------------

    @property
    def account_number(self) -> int:
        """Returns the account number of the client's Bank Account.
        
        Returns:
            int: The account number of the Bank Account.
        """

        return self.__account_number
    
    @property
    def client_number(self) -> int:
        """Returns the client number of the client's Bank Account.
        
        Returns:
            int: The client number of the Bank Account.
        """

        return self.__client_number

    @property
    def balance(self) -> float:
        """Returns the value of the Bank Account's current balance.
        
        Returns:
            float: The current balance of the Bank Account.
        """

        return self.__balance

    #region -------------- Methods --------------

    def update_balance(self, amount: float) -> None:
        """Updates the Bank Account's balance based on amount given.
        
        Args:
            amount (float): The amount to change the Bank Account's
                balance.

        Example:
            >>> bank_account.update_balance(200) # int
            >>> bank_account.update_balance("200") # str
            >>> bank_account.update_balance(200.00) # float
        """

        # Converts value to string and using the .isdigit() function.
        # Function returns true if all characters in value are 
        # decimal characters and digits.
        # https://docs.python.org/3/library/stdtypes.html#str.isdigit
        if str(amount).isdigit():
            amount = float(amount)

        if amount > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction ${amount:,.2f}: "
                        f"on account {self.account_number}.")

        if isinstance(amount, float):
            self.__balance += amount

        if self.balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self.balance:,.2f}: "
                        f"on account {self.account_number}.")

    def deposit(self, amount: float) -> None:
        """Deposits the given amount to the Bank Account's balance.

        Args:
            amount (float): The amount to deposit to the Bank Account.

        Raises:
            ValueError: If the amount is not numeric, or the amount is 
                not positive.

        Example:
            >>> bank_account.deposit(200.00)
        """

        if not isinstance(amount, float):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
    
        if amount < 0:
            raise ValueError(
                f"Deposit amount: ${amount:,.2f} must be positive.")
        
        self.update_balance(amount)
    
    def withdraw(self, amount: float) -> None:
        """Withdraws the given amount from the Bank Account's balance.

        Args:
            amount (float): The amount to withdraw from the Bank 
                Account's balance.

        Raises:
            ValueError: If the amount is not numeric, the amount is 
                not positive, or if the withdrawal amount is greater 
                than the current balance.

        Example:
            >>> bank_account.withdraw(200.00)
        """

        if not isinstance(amount, float):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")

        if amount < 0:
            raise ValueError(
                f"Withdrawal amount: ${amount:,.2f} must be positive.")

        if amount > self.balance:
            raise ValueError(
                f"Withdrawal amount: ${amount:,.2f}" 
                f" must not exceed the account balance: ${self.balance:,.2f}")
        
        self.update_balance(-amount)

    #region -------------- Abstract Method --------------
    
    @abstractmethod
    def get_service_charges(self) -> float:
        """Returns the calculated service charge the Bank Account will
        incur.

        Returns:
            float: The calculated service charge of the Bank Account.
        """

        pass

    #region -------------- Subject Methods --------------
    
    def attach(self, observer: Observer) -> None:
        """Attaches an observer to the current subject.
        
        Args:
            observer (Observer): An observer to add from the subject.
        """

        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Detaches an observer to the current subject.
        
        Args:
            observer (Observer): An observer to remove from the subject. 
        """

        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """Alerts all registered observers of a state change. 
        
        Args:
            message (str): The message to send to registered observers.
        """

        for observer in self._observers:
            observer.update(message)

    #region -------------- String Method -------------- 

    def __str__(self) -> str:
        """Creates a formatted message detailing the Bank Account's 
        values and details.
        
        Returns:
            str: A string displaying the Bank Account's details.
        """

        # Variables to shorten the length of line 170 below. 
        account_number = self.account_number
        balance = self.balance

        return f"Account Number: {account_number} Balance: ${balance:,.2f}\n"
