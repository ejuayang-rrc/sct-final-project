"""A client program written to verify implementation 
of a user interface.

Example:
    python A04_main.py
"""

__author__ = "ACE Faculty"
__version__ = "4.02.2025"
__credits__ = "Elijah Juayang"

# REQUIREMENT - add import statements
from user_interface.client_lookup_window import ClientLookupWindow

# GIVEN:
from PySide6.QtWidgets import QApplication

# GIVEN:
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mainWindow = ClientLookupWindow()
    mainWindow.show()
    sys.exit(app.exec())
