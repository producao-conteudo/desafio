"""Base repositories."""
from abc import ABC, abstractmethod

from entities import Card, Entity, Tag


class Repository(ABC):
    """Base class for repositories."""

    entity = Entity

    @abstractmethod
    def save(self):
        """Persist a new entity."""

    @abstractmethod
    def get(self):
        """Retrieve an entity."""

    @abstractmethod
    def update(self):
        """Update an entity and persist the changes."""

    @abstractmethod
    def remove(self):
        """Remove an entity and persist the changes."""

    @abstractmethod
    def list(self):
        """Retrieve a list of cards."""


class TagRepository(Repository):
    """Base class for tag repository."""

    entity = Tag


class CardRepository(Repository):
    """Base class for card repository."""

    entity = Card
