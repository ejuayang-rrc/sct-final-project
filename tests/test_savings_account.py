"""Unit tests to test the the SavingsAccount and it's methods.

Example:
    python -m unittest tests/test_savings_account.py
    python -m unittest -v tests/test_savings_account.py
"""

__author__ = "Elijah Juayang"
__version__ = "2.12.2025"

from bank_account.savings_account import SavingsAccount
from datetime import date, timedelta
import unittest

class TestSavingsAccount(unittest.TestCase):
    """Unit tests for the SavingsAccount class and it's methods."""

    def setUp(self):
        """Pre-made SavingsAccount object to save code and space for 
        tests.
        """

        # SavingsAccount Attributes
        self.account_number = 123456
        self.client_number = 246810
        self.balance = 1500.0
        self.date_created = date(2002, 1, 27)
        self.minimum_balance = 500.0

        # SavingsAccount Class
        self.savings_account = SavingsAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.minimum_balance
        )

    #region -------------- Initializing Object --------------
    
    def test_initialize_chequing_account_set_attributes_to_input_values(self):
        """Tests if input values are properly set to attributes when 
        initializing the class.
        """

        # ASSERT:
        # Superclass Attributes
        self.assertEqual(
            123456, self.savings_account._BankAccount__account_number)
        self.assertEqual(
            246810, self.savings_account._BankAccount__client_number)
        self.assertEqual(
            1500.00, self.savings_account._BankAccount__balance)
        self.assertEqual(
            date(2002, 1, 27), self.savings_account._date_created)
        
        # Subclass Attributes
        self.assertEqual(
            500.0, self.savings_account._SavingsAccount__minimum_balance)
        
    def test_initialize_minimum_balance_invalid_except_to_set_value(self):
        """Tests if minimum balance is set to a pre-made value if 
        given an invalid type.
        """

        # ARRANGE:
        self.minimum_balance = "Invalid"

        # ACT:
        savings_account = SavingsAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.minimum_balance
        )

        # ASSERT:
        self.assertEqual(50.0, savings_account._SavingsAccount__minimum_balance)
        
    #region -------------- Methods --------------

    def test_get_service_charges_balance_greater_than_minimum_balance(self):
        """Tests if get_service_charges returns a pre-set value when
        balance is greater than minimum balance.
        """

        # ACT:
        actual = self.savings_account.get_service_charges()

        # ASSERT:
        expected = 0.5
        self.assertEqual(expected, actual)

    def test_get_service_charges_balance_equal_to_minimum_balance(self):
        """Tests if get_service_charges returns a pre-set value when
        balance is equal to minimum balance.
        """

        self.balance = 500.0

        savings_account = SavingsAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.minimum_balance
        )

        # ACT:
        actual = savings_account.get_service_charges()

        # ASSERT:
        expected = 0.5
        self.assertEqual(expected, actual)

    def test_get_service_charges_balance_less_than_minimum_balance(self):
        """Tests if get_service_charges returns a pre-set value when
        balance is less than minimum balance.
        """

        self.balance = 250.0

        savings_account = SavingsAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.minimum_balance
        )

        # ACT:
        actual = savings_account.get_service_charges()

        # ASSERT:
        expected = 1.0
        self.assertEqual(expected, actual)

    #region -------------- String Method -------------- 

    def test_string_method_returns_proper_formatted_string(self):
        """Test if string dunder method returns expected formatted 
        string method.
        """

        # ACT:
        actual = self.savings_account.__str__()

        # ASSERT:
        expected = ("Account Number: 123456 Balance: $1,500.00\n"
                    "Minimum Balance: $500.00 Account Type: Savings")
        self.assertEqual(expected, actual)
