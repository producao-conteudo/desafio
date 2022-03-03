"""Base repositories."""
from abc import ABC, abstractmethod

from entities import Card, Entity, Tag


class Repository(ABC):
    """Base class for repositories."""

    entity = Entity

    @abstractmethod
    def save(self, entity):
        """Persist a new entity."""

    @abstractmethod
    def get(self, id):  # noqa: VNE003
        """Retrieve an entity."""

    @abstractmethod
    def update(self, id, **kwargs):  # noqa: VNE003
        """Update an entity and persist the changes."""

    @abstractmethod
    def remove(self, id):  # noqa: VNE003
        """Remove an entity and persist the changes."""

    @abstractmethod
    def list(self):
        """Retrieve a list of entities."""


class TagRepository(Repository):
    """Base class for tag entities repository."""

    entity = Tag


class CardRepository(Repository):
    """Base class for card entities repository."""

    entity = Card
