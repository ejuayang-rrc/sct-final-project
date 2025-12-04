"""Unit tests to test the the BankAccount and it's methods.

NOTE: Unit tests do not work anymore since the BankAccount class was
made to be an abstract class.

Example:
    python -m unittest tests/test_bank_account.py
    python -m unittest -v tests/test_bank_account.py
"""

__version__ = "1.23.2025"
__credits__ = "Elijah Juayang"

import unittest
from bank_account.bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    """Unit tests for the BankAccount class, testing it's 
    accessors and methods.
    """

    def setUp(self):
        """Pre-made Client object to save code and space for tests."""

        account_number = 123456
        client_number = 246810
        balance = 1500

        self.bank_account = \
            BankAccount(account_number, client_number, balance)
        
    #region -------------- Initializing Object --------------

    def test_initialize_bank_account_set_attributes_to_input_values(self):
        """Tests if input values are properly set to attributes when 
        initializing the class.
        """

        # Assert:
        self.assertEqual(123456, self.bank_account._BankAccount__account_number)
        self.assertEqual(246810, self.bank_account._BankAccount__client_number)
        self.assertEqual(1500.00, self.bank_account._BankAccount__balance)

    #region -------------- Exception Raising __init__ --------------

    def test_initialize_bank_account_invalid_balance_value_set_to_zero(self):
        """Tests if the balance attribute sets to a value of 0 when 
        given a non-numeric balance value.
        """

        # Arrange:
        account_number = 123456
        balance = "One Million"
        client_number = 246810

        # Act:
        bank_account = BankAccount(account_number, client_number, balance)

        # Assert:
        self.assertEqual(0, bank_account._BankAccount__balance)

    def test_initialize_bank_account_invalid_account_value_raise_error(self):
        """Tests for a ValueError when given a non-numeric 
        account number with the correct error message.
        """

        # Arrange:
        account_number = "Three"
        balance = 1500
        client_number = 246810

        # Act:
        with self.assertRaises(ValueError) as context:
            BankAccount(account_number, client_number, balance)

        # Assert:
        expected = "Account number must be an integer."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_initialize_bank_account_invalid_client_value_raise_error(self):
        """Tests for a ValueError when given a non-numeric 
        client number with the correct error message.
        """

        # Arrange:
        account_number = 123456
        balance = 1500
        client_number = "Three"

        # Act:
        with self.assertRaises(ValueError) as context:
            BankAccount(account_number, client_number, balance)

        # Assert:
        expected = "Client number must be an integer."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    #region -------------- Accessors -------------- 

    def test_bank_account_account_number_accessor_returns_correct_value(self):
        """Tests to see if the accessor for the account number attribute
        returns the value of the object's account number attribute.
        """

        # Act:
        actual = self.bank_account.account_number

        # Assert:
        expected = 123456
        self.assertEqual(expected, actual)

    def test_bank_account_client_number_accessor_returns_correct_value(self):
        """Tests to see if the accessor for the client number attribute
        returns the value of the object's client number attribute.
        """

        # Act:
        actual = self.bank_account.client_number

        # Assert:
        expected = 246810
        self.assertEqual(expected, actual)

    def test_bank_account_balance_accessor_returns_correct_value(self):
        """Tests to see if the accessor for the balance attribute
        returns the value of the object's balance attribute."""

        # Act:
        actual = self.bank_account.balance

        # Assert:
        expected = 1500
        self.assertEqual(expected, actual)

    #region -------------- Update Balance Method -------------- 

    def test_update_balance_method_updated_balance_positive_amount_value(self):
        """Tests if the update balance method correctly updates the 
        balance attribute when positive amount is received.
        """

        # Act:
        self.bank_account.update_balance(500.99)

        # Assert:
        actual = self.bank_account._BankAccount__balance
        expected = 2000.99
        self.assertEqual(expected, actual)

    def test_update_balance_method_updated_balance_negative_amount_value(self):
        """Tests if the update balance method correctly updates the 
        balance attribute when negative amount is received.
        """

        # Act:
        self.bank_account.update_balance(-250.01)

        # Assert:
        actual = self.bank_account._BankAccount__balance
        expected = 1249.99
        self.assertEqual(expected, actual)

    def test_update_balance_method_unchanged_invalid_amount_value(self):
        """Tests if the balance attribute value remains unchanged 
        when the update balance method receives an amount that is 
        non-numeric.
        """

        # Act:
        self.bank_account.update_balance("One Million")

        # Assert:
        actual = self.bank_account._BankAccount__balance
        expected = 1500
        self.assertEqual(expected, actual)

    #region -------------- Deposit Method -------------- 

    def test_deposit_method_valid_amount_value_balance_updated(self):
        """Tests if the BankAccount object's balance attribute is 
        updated correctly when a valid amount is provided to the deposit 
        method.
        """

        # Act:
        self.bank_account.deposit(500.99)

        # Assert:
        actual = self.bank_account._BankAccount__balance
        expected = 2000.99
        self.assertEqual(expected, actual)

    def test_deposit_method_non_numeric_amount_value_raise_error(self):
        """Tests if a ValueError is raised when a non-numeric amount 
        value is provided to the deposit method with the correct error 
        message.
        """

        # Act:
        with self.assertRaises(ValueError) as context:
            self.bank_account.deposit("One Million")

        # Assert:
        expected = "Deposit amount: One Million must be numeric."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_deposit_method_negative_amount_value_raise_error(self):
        """Tests if a ValueError is raised when negative amount is 
        provided to the deposit method with the correct error message.
        """

        # Act:
        with self.assertRaises(ValueError) as context:
            self.bank_account.deposit(-250.01)

        # Assert:
        expected = "Deposit amount: $-250.01 must be positive."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    #region -------------- Withdraw Method -------------- 

    def test_withdraw_method_valid_amount_value_balance_updated(self):
        """Tests if the BankAccount object's balance is updated 
        correctly when a valid amount is provided to the withdraw 
        method.
        """

        # Act:
        self.bank_account.withdraw(250.01)

        # Assert:
        actual = self.bank_account._BankAccount__balance
        expected = 1249.99
        self.assertEqual(expected, actual)

    def test_withdraw_method_non_numeric_amount_value_raise_error(self):
        """Tests if a ValueError is raised when a non-numeric amount 
        value is provided to the withdraw method with the correct error 
        message.
        """

        # Act:
        with self.assertRaises(ValueError) as context:
            self.bank_account.withdraw("One Million")

        # Assert:
        expected = "Withdraw amount: One Million must be numeric."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_withdraw_method_negative_amount_value_raise_error(self):
        """Tests if a ValueError is raised when negative amount is 
        provided to the withdraw method with the correct error message.
        """

        # Act:
        with self.assertRaises(ValueError) as context:
            self.bank_account.withdraw(-250.01)

        # Assert:
        expected = "Withdrawal amount: $-250.01 must be positive."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_withdraw_method_amount_exceeds_balance_raise_error(self):
        """Tests if a ValueError is raised when the amount provided to 
        the withdraw method exceeds the bank account's balance with the 
        correct error message.
        """

        # Act:
        with self.assertRaises(ValueError) as context:
            self.bank_account.withdraw(2500.00)

        # Assert:
        expected = "Withdrawal amount: $2,500.00" \
            " must not exceed the account balance: $1,500.00"
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    #region -------------- String Method -------------- 

    def test_string_method_returns_string_with_expected_format(self):
        """Tests if the __str__ method of the BankAccount object returns 
        a properly formatted string with the correct values and format.
        """

        # Act:
        actual = self.bank_account.__str__()

        # Assert:
        expected = "Account Number: 123456 Balance: $1,500.00"
        self.assertEqual(expected, actual)
    