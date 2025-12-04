"""This module defines functions to access and maintain bank account and
client data from files.
"""

__author__ = "ACE Faculty"
__version__ = "4.01.2025"
__credits__ = "Elijah Juayang"

import os
import sys

# THIS LINE IS NEEDED SO THAT THE GIVEN TESTING 
# CODE CAN RUN FROM THIS DIRECTORY.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from bank_account import *
from client.client import Client
import csv
from datetime import date
import logging

# **********************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE
 
# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))
 
# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')
 
# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok = True)
 
# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')
 
# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s')
 
# Given File Path Code:
# Designed to locate the input files without providing any directory 
# structure

# Construct the absolute path to the data directory at the root of the 
# project
data_dir = os.path.join(root_dir, 'data')
 
# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
 
# END GIVEN LOGGING AND FILE ACCESS CODE
# **********************************************************************

def load_data() -> tuple[dict, dict]:
    """Populates a client dictionary and an account dictionary with 
    corresponding data from files within the data directory.

    Returns:
        tuple: containing client dictionary and account dictionary.
    """

    client_listing = {}
    accounts = {}

    # READ CLIENT DATA 
    with open(clients_csv_path, "r", newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for record in reader:
            try:
                client_listing[int(record["client_number"])] = \
                    Client(int(record["client_number"]), record["first_name"], 
                           record["last_name"], record["email_address"])
            except ValueError as e:
                logging.error(f"Unable to create client: {e}")

    # READ ACCOUNT DATA
    with open(accounts_csv_path, "r", newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for record in reader:
            try:
                account_number = int(record["account_number"])
                client_number = int(record["client_number"])
                balance = float(record["balance"])
                date_created = date.fromisoformat(record["date_created"])
                account_type = record["account_type"]

                # Adds the record to accounts if client exists.
                if client_number in client_listing:
                    match account_type:
                        case "ChequingAccount":
                            overdraft_limit = float(record["overdraft_limit"])
                            overdraft_rate = float(record["overdraft_rate"])

                            accounts[account_number] = ChequingAccount(
                                account_number, client_number, balance, 
                                date_created, overdraft_limit, overdraft_rate)
                            
                        case "InvestmentAccount":
                            management_fee = float(record["management_fee"])

                            accounts[account_number] = InvestmentAccount(
                                account_number, client_number, balance, 
                                date_created, management_fee)
                            
                        case "SavingsAccount":
                            minimum_balance = float(record["minimum_balance"])

                            accounts[account_number] = SavingsAccount(
                                account_number, client_number, balance, 
                                date_created, minimum_balance)

                        case _:
                            raise ValueError("Not a valid account type.")

                # This runs if client doesn't match existing clients.
                else: 
                    logging.error(f"Bank Account: {account_number} contains "
                                  f"invalid Client Number: {client_number}")

            except ValueError as e:
                logging.error(f"Unable to create bank account: {e}")

    # RETURN STATEMENT
    return (client_listing, accounts)
    
def update_data(updated_account: BankAccount) -> None:
    """A function to update the accounts.csv file with balance 
    data provided in the BankAccount argument.

    Args:
        updated_account (BankAccount): A bank account containing an 
            updated balance.
    """

    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        
        for row in reader:
            account_number = int(row['account_number'])

            # Check if the account number is in the dictionary
            if account_number == updated_account.account_number:

                # Update the balance column with the new balance from 
                # the dictionary
                row['balance'] = updated_account.balance

            updated_rows.append(row)

    # Write the updated data back to the CSV
    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)

# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients, accounts = load_data()

    print("=========================================")

    for client in clients.values():
        print(client)
        print(f"\n{client.client_number} Accounts\n=============")

        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")

        print("=========================================")
    