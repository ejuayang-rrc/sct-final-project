"""This module defines a class representing a Client."""

__author__ = "Elijah Juayang"
__version__ = "3.10.2025"

from email_validator import validate_email, EmailNotValidError 
from datetime import date
from utility.file_utils import simulate_send_email
from patterns.observer.observer import Observer

class Client(Observer):
    """A class representing an client."""
    
    #region -------------- Initializing Object --------------

    def __init__(self, client_number: int, first_name: str, 
                 last_name: str, email_address: str):
        """Initializes an instance of the Client class.
         
        Args:
            client_number (int): A value representing the Client number.
            first_name (str): The Client's first name.
            last_name (str): The Client's last name.
            email_address (str): The Client's email address.

        Raises:
            ValueError: Raised when first or last name is blank, or if
                client number is not an integer value.
        """

        if not isinstance(client_number, int):
            raise ValueError("Client Number must be an integer.")
        
        if len(first_name.strip()) == 0:
            raise ValueError("First name cannot be blank.")
        
        if len(last_name.strip()) == 0:
            raise ValueError("Last name cannot be blank.")
        
        # Except changes email address to a set value if invalid.
        try:
            validate_email(email_address)
        except EmailNotValidError:
            email_address = "email@pixell-river.com"

        self.__client_number = client_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email_address = email_address

    #region -------------- Accessors --------------

    @property
    def client_number(self) -> int:
        """Returns the value of the Client's client number.
        
        Returns:
            int: A value representing the client number.
        """

        return self.__client_number
    
    @property
    def first_name(self) -> str:
        """Returns the first name of the Client.
        
        Returns:
            str: The Client's first name.
        """

        return self.__first_name
    
    @property
    def last_name(self) -> str:
        """Returns the last name of the Client.
        
        Returns:
            str: The Client's last name.
        """

        return self.__last_name
    
    @property
    def email_address(self) -> str:
        """Returns the email address of the Client.
        
        Returns:
            str: The client's email address.
        """

        return self.__email_address
    
    #region -------------- Special Methods --------------

    def __str__(self) -> str:
        """Creates a message with the Client's name, number, and email.
        
        Returns:
            str: A string displaying the Client's details.
        """

        return (f"{self.last_name}, {self.first_name} "
                f"[{self.client_number}] - {self.email_address}")
    
    #region -------------- Method --------------

    def update(self, message: str) -> None:
        """This method performs an action when the Observer is notified.
        
        Args:
            message (str): The notification message.
        """

        subject = f"ALERT: Unusual Activity: {date.today()}"
        message = (f"Notification for {self.client_number}: {self.first_name} "
                   f"{self.last_name}: {message}")

        simulate_send_email(self.email_address, subject, message)
