""""A client program written to verify correctness of 
the BankAccount and Client classes.

Example:
    python A01_main.py
"""

__author__ = "ACE Faculty"
__version__ = "1.22.2025"
__credits__ = "Elijah Juayang"

from bank_account.bank_account import BankAccount
from client.client import Client

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Client classes.
    """ 

    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled. When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.
    client = Client(403650, "John", "Doe", "johndoe@gmail.com")

    # 2. Declare a variable that could store a BankAccount instance.    
    # Define the variable with an initial value of None.    
    bank_account = None

    # 3. Using the the variable declared in step 2, code a statement    
    # to instantiate a BankAccount object.    
    # Use any integer value for the BankAccount number.    
    # Use the client number used to create the Client object in step 1 for the    
    # BankAccount's client number.    
    # Use a floating point value for the balance. 
    bank_account = BankAccount(204206, 403650, 1505.25)

    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use an INVALID value (non-float) for the balance. 
    invalid_bank = BankAccount(304076, 403650, "Rock")

    # 5. Code a statement which prints the Client instance created in step 1. 
    # Code a statement which prints the BankAccount instance created in step 3.
    print(client.__str__())
    print(bank_account.__str__())

    # 6. Attempt to deposit a non-numeric value into the BankAccount created in step 3.
    try:
        bank_account.deposit("Horse")
    except ValueError as exception:
        print(exception)

    # 7. Attempt to deposit a negative value into the BankAccount created in step 3. 
    try:
        bank_account.deposit(-30.00)
    except ValueError as exception:
        print(exception)

    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount create in step 3. 
    bank_account.withdraw(400.00)

    # 9. Attempt to withdraw a non-numeric value from the BankAccount create in step 3. 
    try:
        bank_account.withdraw("Horse")
    except ValueError as exception:
        print(exception)

    # 10. Attempt to withdraw a negative value from the BankAccount create in step 3. 
    try:
        bank_account.withdraw(-650.00)
    except ValueError as exception:
        print(exception)

    # 11. Attempt to withdraw a value from the BankAccount create in step 3 which 
    # exceeds the current balance of the account. 
    try:
        bank_account.withdraw(2090.50)
    except ValueError as exception:
        print(exception)

    # 12. Code a statement which prints the BankAccount instance created in step 3. 
    print(bank_account.__str__())

if __name__ == "__main__":
    main()
