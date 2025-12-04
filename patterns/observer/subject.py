"""This module defines the Subject class."""

__version__ = "3.10.2025"
__credits__ = "Elijah Juayang"

from abc import ABC, abstractmethod
from patterns.observer.observer import Observer

class Subject(ABC):
    """This class represents a subject."""

    def __init__(self):
        """Initializes an instance of the Subject class."""

        self._observers = []

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """Attaches an observer to the current subject.
        
        Args:
            observer (Observer): An observer to add from the subject.
        """

        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """Detaches an observer to the current subject.
        
        Args:
            observer (Observer): An observer to remove from the subject. 
        """

        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        """Alerts all registered observers of a state change. 
        
        Args:
            message (str): The message to send to registered observers.
        """

        pass
