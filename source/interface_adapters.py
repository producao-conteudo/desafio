"""Data access interface adapters for the use cases and frameworks/drivers."""
from abc import ABC, abstractmethod


class TagRepository(ABC):
    """Base class for tag repository."""

    @abstractmethod
    def save(self):
        """Persist a new tag."""

    @abstractmethod
    def get(self):
        """Retrieve a tag."""

    @abstractmethod
    def update(self):
        """Update a tag and persist the changes."""

    @abstractmethod
    def remove(self):
        """Remove a tag and persist the changes."""


class CardRepository(ABC):
    """Base class for card repository."""

    @abstractmethod
    def save(self):
        """Persist a new card."""

    @abstractmethod
    def get(self):
        """Retrieve a card."""

    @abstractmethod
    def update(self):
        """Update a card and persist the changes."""

    @abstractmethod
    def remove(self):
        """Remove a card and persist the changes."""

    @abstractmethod
    def list(self):
        """Retrieve a list of cards."""
