"""This module defines the Observer class."""

__version__ = "3.09.2025"
__credits__ = "Elijah Juayang"

from abc import ABC, abstractmethod

class Observer(ABC):
    """This class represents an observer that looks for changes in the 
    subject.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """This method performs an action when the Observer is notified.
        
        Args:
            message (str): The notification message.
        """

        pass
    