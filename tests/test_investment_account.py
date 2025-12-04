"""Unit tests to test the the InvestmentAccount and it's methods.

Example:
    python -m unittest tests/test_investment_account.py
    python -m unittest -v tests/test_investment_account.py
"""

__author__ = "Elijah Juayang"
__version__ = "2.11.2025"

from bank_account.investment_account import InvestmentAccount
from datetime import date, timedelta
import unittest

class TestInvestmentAccount(unittest.TestCase):
    """Unit tests for the InvestmentAccount class and it's methods."""

    def setUp(self):
        """Pre-made InvestmentAccount object to save code and space for 
        tests.
        """

        # InvestmentAccount Attributes
        self.account_number = 123456
        self.client_number = 246810
        self.balance = 1500.0
        self.date_created = date(2002, 1, 27)
        self.management_fee = 4.75

        # InvestmentAccount Class
        self.investment_account = InvestmentAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.management_fee
        )

    #region -------------- Initializing Object --------------

    def test_initialize_chequing_account_set_attributes_to_input_values(self):
        """Tests if input values are properly set to attributes when 
        initializing the class.
        """

        # ASSERT:
        # Superclass Attributes
        self.assertEqual(
            123456, self.investment_account._BankAccount__account_number)
        self.assertEqual(
            246810, self.investment_account._BankAccount__client_number)
        self.assertEqual(
            1500.00, self.investment_account._BankAccount__balance)
        self.assertEqual(
            date(2002, 1, 27), self.investment_account._date_created)
        
        # Subclass Attributes
        self.assertEqual(
            4.75, self.investment_account._InvestmentAccount__management_fee)
    
    #region -------------- Init Method Exceptions --------------

    def test_initialize_management_fee_invalid_except_to_set_value(self):
        """Test if management fee is set to a pre-made value when given 
        an invalid type.
        """

        # ARRANGE:
        self.management_fee = "Invalid"

        # ACT:
        investment_account = InvestmentAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.management_fee
        )

        # ASSERT:
        self.assertEqual(
            2.55, investment_account._InvestmentAccount__management_fee)
        
    #region -------------- Methods --------------

    def test_get_service_charges_created_more_than_ten_years(self):
        """Test if value returned is set to a pre-made value when date 
        created is more than 10 years ago.
        """

        # ACT:
        actual = self.investment_account.get_service_charges()

        # ASSERT:
        expected = 0.5
        self.assertEqual(expected, actual)

    def test_get_service_charges_created_exactly_ten_years(self):
        """Test if value returned is set to a pre-made value when date 
        created is exactly 10 years ago.
        """

        # ARRANGE:
        self.date_created = date.today() - timedelta(days = 10 * 365.25)

        investment_account = InvestmentAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.management_fee
        )

        # ACT:
        actual = investment_account.get_service_charges()

        # ASSERT:
        expected = 5.25
        self.assertEqual(expected, actual)
        
    def test_get_service_charges_created_last_ten_years(self):
        """Test if value returned is a calculated value when date
        created is within the last 10 years.
        """

        # ARRANGE:
        self.date_created = date.today()

        investment_account = InvestmentAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.management_fee
        )

        # ACT:
        actual = investment_account.get_service_charges()

        # ASSERT:
        expected = 5.25
        self.assertEqual(expected, actual)

    #region -------------- String Method -------------- 

    def test_string_method_returns_proper_format_more_than_ten_years(self):
        """Tests if returned string displays waived management fee when 
        date created is more than 10 years ago.
        """

        # ACT:
        actual = self.investment_account.__str__()

        # ASSERT:
        expected = ("Account Number: 123456 Balance: $1,500.00\n"
                    "Date Created: 2002-01-27 Management Fee: Waived Account "
                    "Type: Investment")
        self.assertEqual(expected, actual)

    def test_string_method_returns_proper_format_last_ten_years(self):
        """Tests if returned string displays management fee when date 
        created is within the last 10 years.
        """

        # ARRANGE:
        self.date_created = date(2020, 1, 27)

        investment_account = InvestmentAccount(
            self.account_number,
            self.client_number,
            self.balance,
            self.date_created,
            self.management_fee
        )

        # ACT:
        actual = investment_account.__str__()

        # ASSERT:
        expected = ("Account Number: 123456 Balance: $1,500.00\nDate Created: "
                    "2020-01-27 Management Fee: $4.75 Account Type: Investment")
        self.assertEqual(expected, actual)
