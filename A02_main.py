"""Description: A client program written to verify correctness of 
the BankAccount sub classes.

Example:
    python A02_main.py
"""

__author__ = "ACE Faculty"
__version__ = "2.12.2025"
__credits__ = "Elijah Juayang"

# 1. Import all BankAccount types using the bank_account package
from bank_account import *

# 1b. Import date from datetime
# NOTE: I added timedelta for InvestmentAccount instructions.
from datetime import date, timedelta

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing_account = ChequingAccount(
    20051208,
    20240125,
    -550.00,
    date(1995, 12, 8),
    -200,
    0.1
)

# 3. Print the ChequingAccount created in step 2.
print(chequing_account.__str__())

# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing_account.get_service_charges())

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
chequing_account.deposit(650.0)

# 4b. Print the ChequingAccount
print(chequing_account.__str__())

# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing_account.get_service_charges())

# Prints a very long line in terminal.
long_print_line = "=" * 51
print(long_print_line)

# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
savings_account = SavingsAccount(
    20101305,
    20240125,
    550.0,
    date(1995, 12, 8),
    100.0
)

# 6. Print the SavingsAccount created in step 5.
print(savings_account.__str__())

# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(savings_account.get_service_charges())

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
savings_account.withdraw(500.0)

# 7b. Print the SavingsAccount.
print(savings_account.__str__())

# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(savings_account.get_service_charges())
print(long_print_line)

# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
date_last_five_years = date.today() - timedelta(days = 3 * 365.25)

investment_account = InvestmentAccount(
    20101305,
    20240125,
    550.0,
    date_last_five_years,
    5.75
)

# 9a. Print the InvestmentAccount created in step 8.
print(investment_account.__str__())

# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(investment_account.get_service_charges())

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
date_ten_years_ago = date.today() - timedelta(days = 15 * 365.25)

old_investment_account = InvestmentAccount(
    20788878,
    20234534,
    550.0,
    date_ten_years_ago,
    5.75
)

# 11a. Print the InvestmentAccount created in step 10.
print(old_investment_account.__str__())

# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(old_investment_account.get_service_charges())
print(long_print_line)

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
bank_accounts = [
    chequing_account,
    savings_account,
    investment_account,
    old_investment_account
]

for account in bank_accounts:
    account.withdraw(account.get_service_charges())

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
for account in bank_accounts:
    print(account.__str__())
