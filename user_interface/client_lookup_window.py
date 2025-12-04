"""This module defines the Client Lookup window."""

__author__ = "ACE Faculty"
__version__ = "4.24.2025"
__credits__ = "Elijah Juayang"

from datetime import date
from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot
from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data, update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """A class used to display and lookup clients and their details."""

    def __init__(self):
        """Initializes a new instance of the ClientLookup window."""

        super().__init__()

        self.__client_listing, self.__accounts = load_data()

        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
        self.filter_button.clicked.connect(self.__on_filter_clicked) 

    @Slot()
    def __on_lookup_client(self):
        """Obtains the client requested from the user's input, then 
        displays a record of the client's bank accounts on-screen.
        """

        client_number = self.client_number_edit.text()

        # Client number input verification.
        try:
            client_number = int(client_number)
        except ValueError:
            QMessageBox.information(self, "Input Error", 
                "The client number must be a numeric value.")
            self.reset_display()
            return
        
        if not client_number in self.__client_listing:
            QMessageBox.information(self, "Not Found", 
                f"Client number: {client_number} not found.")
            self.reset_display()
            return
        
        self.client_info_label.setText(
            f"Client Name: {self.__client_listing[client_number].first_name} "
            f"{self.__client_listing[client_number].last_name}")

        # Displays each bank account a client owns.
        for account in self.__accounts.values():
            if self.__client_listing[client_number].client_number == \
                account.client_number:
                row = self.account_table.rowCount()
                self.account_table.insertRow(row)
                
                account_number_item = QTableWidgetItem(
                    str(account.account_number))
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                date_created_item = QTableWidgetItem(str(account._date_created))
                account_type_item = QTableWidgetItem(account.__class__.__name__)

                account_number_item.setTextAlignment(Qt.AlignCenter)
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                date_created_item.setTextAlignment(Qt.AlignCenter)
                account_type_item.setTextAlignment(Qt.AlignCenter)

                self.account_table.resizeColumnsToContents()
                self.account_table.setItem(row, 0, account_number_item)
                self.account_table.setItem(row, 1, balance_item)
                self.account_table.setItem(row, 2, date_created_item)
                self.account_table.setItem(row, 3, account_type_item)

                self.__toggle_filter(False)

    @Slot()
    def __on_text_changed(self):
        """Clears all bank account records."""

        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int):
        """Identifies the selected account then transfers control to
        the Account Details window.

        Args:
            row (int): Row that has been clicked on.
            column (int): Column that has been clicked on.
        """

        account_number = int(self.account_table.item(row, 0).text())

        if account_number in self.__accounts:
            window = AccountDetailsWindow(self.__accounts[account_number])
            window.balance_updated.connect(self.__update_data)
            window.exec_()
        elif account_number == None or account_number == "":
            QMessageBox.information(
                self, "Invalid Selection", "Please select a valid record.")
        else:
            QMessageBox.information(self, "No Bank Account", 
                "Bank Account selected does not exist.")
            
    def __update_data(self, account: BankAccount):
        """Updates bank account data based on updates made in 
        another window.

        Args:
            account (BankAccount): A bank account containing an 
                updated balance.
        """
        
        for row in range(self.account_table.rowCount()):
            if str(account.account_number) == \
                self.account_table.item(row, 0).text():

                # Update table in window.
                self.account_table.item(row, 1).setText(
                    f"${account.balance:,.2f}")

                # Update array of accounts.
                self.__accounts[account.account_number] = account

                # Update CSV file.
                update_data(account)

    def __on_filter_clicked(self):
        """Filters displayed accounts based on the given input criteria,
        then returns a display of the filtered results.
        """

        if self.filter_button.text() == "Apply Filter":
            search_field = self.filter_combo_box.currentIndex()
            search_text = self.filter_edit.text()

            for row in range(self.account_table.rowCount()):
                if search_text not in \
                    self.account_table.item(row, search_field).text():
                    self.account_table.setRowHidden(row, True)

        self.__toggle_filter(self.filter_button.text() == "Apply Filter")

    def __toggle_filter(self, filter_on: bool):
        """Toggles display of the filter widgets.
        
        Args:
            filter_on (bool): Enables or disables filter widgets.
        """     

        self.filter_button.setEnabled(True)
        self.filter_combo_box.setEnabled(not filter_on)
        self.filter_edit.setEnabled(not filter_on)
        self.filter_button.setText("Reset" if filter_on else "Apply Filter")
        self.filter_label.setText("Data is Currently Filtered." if filter_on 
                                  else "Data is Not Currently Filtered.")
        
        if not filter_on:
            self.filter_combo_box.setCurrentIndex(0)
            self.filter_edit.setText("")

            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)
