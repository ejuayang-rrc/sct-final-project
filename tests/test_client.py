"""Unit tests to test the Client class and it's methods.

Example:
    python -m unittest tests/test_client.py
    python -m unittest -v tests/test_client.py
"""

__version__ = "1.23.2025"
__credits__ = "Elijah Juayang"

import unittest
from client.client import Client

class TestClient(unittest.TestCase):
    """Unit tests for the Client class, testing it's
    accessors and methods.
    """

    def setUp(self):
        """Pre-made Client object to save code and space for tests."""
        
        client_number = 2437
        first_name = "Elijah"
        last_name = "Juayang"
        email_address = "ejuayang@rrc.ca"

        self.client = \
            Client(client_number, first_name, last_name, email_address)

    #region -------------- Initializing Object --------------

    def test_client_set_attributes_to_input_values(self):
        """Tests if the __init__ method for the Client class
        properly sets input values into the object's attributes.
        """

        # Assert:
        self.assertEqual(2437, self.client._Client__client_number)
        self.assertEqual("Elijah", self.client._Client__first_name)
        self.assertEqual("Juayang", self.client._Client__last_name)
        self.assertEqual("ejuayang@rrc.ca", self.client._Client__email_address)
    
    #region -------------- Exception Raising __init__ --------------

    def test_client_raise_exception_invalid_value_client_number(self):
        """Tests if the ValueError with the correct message is 
        raised if the client number attribute is an invalid data type. 
        """

        # Arrange:
        client_number = "three"
        first_name = "Elijah"
        last_name = "Juayang"
        email_address = "ejuayang@rrc.ca"

        # Act:
        with self.assertRaises(ValueError) as context:
            client = \
                Client(client_number, first_name, last_name, email_address)

        # Assert:
        expected = "Client Number must be an integer."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_client_raise_exception_blank_first_name(self):
        """Tests if the ValueError with the correct message is 
        raised if the first name attribute is blank.
        """

        # Arrange:
        client_number = 2437
        first_name = "  "
        last_name = "Juayang"
        email_address = "ejuayang@rrc.ca"

        # Act:
        with self.assertRaises(ValueError) as context:
            client = \
                Client(client_number, first_name, last_name, email_address)

        # Assert:
        expected = "First name cannot be blank."
        actual = str(context.exception)
        self.assertEqual(expected, actual)

    def test_client_raise_exception_blank_last_name(self):
        """Tests if the ValueError with the correct message is 
        raised if the last name attribute is blank.
        """

        # Arrange:
        client_number = 2437
        first_name = "Elijah"
        last_name = "  "
        email_address = "ejuayang@rrc.ca"

        # Act:
        with self.assertRaises(ValueError) as context:
            client = \
                Client(client_number, first_name, last_name, email_address)

        # Assert:
        expected = "Last name cannot be blank."
        actual = str(context.exception)
        self.assertEqual(expected, actual)
        
    def test_client_default_invalid_email_address(self):
        """Tests if the email address attribute is set to a
        pre-set value when given an invalid email address.
        """

        # Arrange:
        client_number = 2437
        first_name = "Elijah"
        last_name = "Juayang"
        email_address = "email.com"

        # Act:
        client = \
            Client(client_number, first_name, last_name, email_address)

        # Assert:
        self.assertEqual(
            "email@pixell-river.com", client._Client__email_address)

    #endregion

    #region -------------- Accessors -------------- 

    def test_client_accessor_returns_client_number_attribute(self):
        """Tests if the accessor for the Client object's client number
        attribute returns the correct value.
        """

        # Act:
        actual = self.client.client_number

        # Assert:
        expected = 2437
        self.assertEqual(expected, actual)

    def test_client_accessor_returns_first_name_attribute(self):
        """Tests if the accessor for the Client object's first name
        attribute returns the correct value.
        """

        # Act:
        actual = self.client.first_name

        # Assert:
        expected = "Elijah"
        self.assertEqual(expected, actual)

    def test_client_accessor_returns_last_name_attribute(self):
        """Tests if the accessor for the Client object's last name
        attribute returns the correct value.
        """

        # Act:
        actual = self.client.last_name

        # Assert:
        expected = "Juayang"
        self.assertEqual(expected, actual)

    def test_client_accessor_returns_email_address_attribute(self):
        """Tests if the accessor for the Client object's email
        address attribute returns the correct value.
        """

        # Act:
        actual = self.client.email_address

        # Assert:
        expected = "ejuayang@rrc.ca"
        self.assertEqual(expected, actual)

    #endregion

    #region -------------- String Method -------------- 

    def test_client_string_method_returns_formatted_string(self):
        """Tests if the __str__ method of the Client object returns a
        properly formatted string with the correct values and format.
        """

        # Act:
        actual = self.client.__str__()

        # Assert:
        expected = "Juayang, Elijah [2437] - ejuayang@rrc.ca"
        self.assertEqual(expected, actual)
