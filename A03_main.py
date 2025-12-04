"""A client program written to verify implementation 
of the Observer Pattern.

Example:
    python A03_main.py
"""

__author__ = "ACE Faculty"
__version__ = "3.11.2025"
__credits__ = "Elijah Juayang"

# 1.  Import all BankAccount types using the bank_account package
#     Import date
#     Import Client
from bank_account import *
from datetime import date
from client.client import Client

# 2. Create a Client object with data of your choice.
client = Client(2002, "Kazuma", "Kiryu", "kamurocho@sega.com")

# 3a. Create a ChequingAccount object with data of your choice, using 
# the client_number of the client created in step 2.
# 3b. Create a SavingsAccount object with data of your choice, using the 
# client_number of the client created in step 2.
bank_accounts = [
    ChequingAccount(2041, 2002, 1000.0, date(1995, 12, 8), -200, 0.1),
    SavingsAccount(2042, 2002, 1500.0, date(1995, 12, 8), 500.0)
]

# 4a. The ChequingAccount and SavingsAccount objects are 'Subject' 
# objects. The Client object is an 'Observer' object. Attach the Client 
# object (created in step 1) to the ChequingAccount object 
# (created in step 2).
bank_accounts[0].attach(client)

# 4b. Attach the Client object (created in step 1) to the SavingsAccount 
# object (created in step 2).
bank_accounts[1].attach(client)

# 5a. Create a second Client object with data of your choice.
client = Client(2025, "Jim", "Carry", "funnyman@mask.com")

# 5b. Create a SavingsAccount object with data of your choice, using 
# the client_number of the client created in this step.
bank_accounts.append(SavingsAccount(2101, 2025, 900.0, date(2020, 6, 20), 25.0))

# 6. Use the ChequingAccount and SavingsAccount objects created 
# in steps 3 and 5 above to perform transactions 
# (deposits and withdraws) which would cause the Subject (BankAccount) 
# to notify the Observer (Client) as well as transactions that would not 
# cause the Subject to notify the Observer. Ensure each 
# BankAccount object performs at least 3 transactions.
# REMINDER: the deposit() and withdraw() methods can raise exceptions
# ensure the methods are invoked using proper exception handling such 
# that any exception messages are printed to the console.
for account in bank_accounts: 
    try:
        account.withdraw(974.1)
    except ValueError as error:
        print(error)

for account in bank_accounts: 
    try:
        account.deposit(15000.0)
    except ValueError as error:
        print(error)
