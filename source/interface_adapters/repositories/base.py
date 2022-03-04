"""Base repositories."""
from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from entities import Card, Entity, Tag


class Repository(ABC):
    """Base class for repositories."""

    entity = Entity

    @abstractmethod
    def save(self, entity: Entity) -> None:
        """Persist a new entity."""

    @abstractmethod
    def get(self, id) -> Optional[Entity]:  # noqa: VNE003
        """Retrieve an entity."""

    @abstractmethod
    def update(self, id: UUID, **kwargs) -> None:  # noqa: VNE003
        """Update an entity and persist the changes."""

    @abstractmethod
    def remove(self, id: UUID) -> None:  # noqa: VNE003
        """Remove an entity and persist the changes."""

    @abstractmethod
    def list(self) -> list[Entity]:
        """Retrieve a list of entities."""


class TagRepository(Repository):
    """Base class for tag entities repository."""

    entity: Entity = Tag


class CardRepository(Repository):
    """Base class for card entities repository."""

    entity: Entity = Card
