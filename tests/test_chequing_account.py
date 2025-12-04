"""Unit tests to test the the ChequingAccount and it's methods.

Example:
    python -m unittest tests/test_chequing_account.py
    python -m unittest -v tests/test_chequing_account.py
"""

__author__ = "Elijah Juayang"
__version__ = "2.10.2025"

from bank_account.chequing_account import ChequingAccount
from datetime import date
import unittest

class TestChequingAccount(unittest.TestCase):
    """Unit tests for the ChequingAccount class and it's methods."""

    def setUp(self):
        """Pre-made ChequingAccount object to save code and space for 
        tests.
        """

        # ChequingAccount Attributes
        self.account_number = 123456
        self.client_number = 246810
        self.balance = 1500.0
        self.date_created = date(2002, 1, 27)
        self.overdraft_limit = -100
        self.overdraft_rate = 0.05

        # ChequingAccount Class
        self.chequing_account = ChequingAccount(
            self.account_number, 
            self.client_number,  
            self.balance,
            self.date_created, 
            self.overdraft_limit, 
            self.overdraft_rate
        )

    #region -------------- Initializing Object --------------

    def test_initialize_chequing_account_set_attributes_to_input_values(self):
        """Tests if input values are properly set to attributes when 
        initializing the class.
        """

        # ASSERT:
        # Superclass Attributes
        self.assertEqual(
            123456, self.chequing_account._BankAccount__account_number)
        self.assertEqual(
            246810, self.chequing_account._BankAccount__client_number)
        self.assertEqual(
            1500.0, self.chequing_account._BankAccount__balance)
        self.assertEqual(
            date(2002, 1, 27), self.chequing_account._date_created)

        # Subclass Attributes
        self.assertEqual(
            -100, self.chequing_account._ChequingAccount__overdraft_limit)
        self.assertEqual(
            0.05, self.chequing_account._ChequingAccount__overdraft_rate)

    #region -------------- Init Method Exceptions --------------

    def test_initialize_overdraft_limit_invalid_except_to_set_value(self):
        """Tests if overdraft_limit attribute is set to a pre-made value 
        when given an invalid type.
        """

        # ARRANGE:
        self.overdraft_limit = "Default"

        # ACT:
        chequing_account = ChequingAccount(
            self.account_number, 
            self.client_number,  
            self.balance,
            self.date_created, 
            self.overdraft_limit, 
            self.overdraft_rate
        )

        # ASSERT:
        self.assertEqual(
            -100, chequing_account._ChequingAccount__overdraft_limit)
        
    def test_initialize_overdraft_rate_invalid_except_to_set_value(self):
        """Tests if overdraft_rate attribute is set to a pre-made value 
        when given an invalid type.
        """

        # ARRANGE:
        self.overdraft_rate = "Default"

        # ACT:
        chequing_account = ChequingAccount(
            self.account_number, 
            self.client_number,  
            self.balance,
            self.date_created, 
            self.overdraft_limit, 
            self.overdraft_rate
        )

        # ASSERT:
        self.assertEqual(
            0.05, chequing_account._ChequingAccount__overdraft_rate)

    def test_initialize_date_created_invalid_except_to_set_value(self):
        """Tests if date_created attribute is set to a pre-made value 
        when given an invalid type.
        """

        # ARRANGE:
        self.date_created = "Set to Today"

        # ACT:
        chequing_account = ChequingAccount(
            self.account_number, 
            self.client_number,  
            self.balance,
            self.date_created, 
            self.overdraft_limit, 
            self.overdraft_rate
        )
        
        # ASSERT:
        expected = date.today()
        self.assertEqual(expected, chequing_account._date_created)

    #region -------------- Methods --------------

    def test_get_service_charges_balance_greater_than_overdraft(self):
        """Tests if service charge will return a pre-made value if 
        balance is greater than overdraft.
        """

        # ACT:
        actual = self.chequing_account.get_service_charges()

        # ASSERT:
        expected = 0.5
        self.assertEqual(expected, actual)

    def test_get_service_charges_balance_less_than_overdraft(self):
        """Tests if service charge will return a calculated value if 
        balance is less than overdraft.
        """

        # ARRANGE:
        self.balance = -600

        chequing_account = ChequingAccount(
            self.account_number, 
            self.client_number,  
            self.balance,
            self.date_created, 
            self.overdraft_limit, 
            self.overdraft_rate
        )

        # ACT:
        actual = chequing_account.get_service_charges()

        # ASSERT:
        expected = 25.5
        self.assertEqual(expected, actual)

    def test_get_service_charges_balance_equal_to_overdraft(self):
        """Tests if service charge will return a pre-made value if 
        balance is equal to overdraft.
        """

        # ARRANGE:
        self.balance = -100

        chequing_account = ChequingAccount(
            self.account_number, 
            self.client_number,  
            self.balance,
            self.date_created, 
            self.overdraft_limit, 
            self.overdraft_rate
        )

        # ACT:
        actual = chequing_account.get_service_charges()

        # ASSERT:
        expected = 0.5
        self.assertEqual(expected, actual)

    #region -------------- String Method -------------- 

    def test_string_method_returns_proper_formatted_string(self):
        """Test if string dunder method returns expected formatted 
        string method.
        """

        # ACT:
        actual = self.chequing_account.__str__()

        # ASSERT:
        expected = ("Account Number: 123456 Balance: $1,500.00\n"
                    "Overdraft Limit: $-100.00 Overdraft Rate: 5.00% "
                    "Account Type: Chequing")
        self.assertEqual(expected, actual)
