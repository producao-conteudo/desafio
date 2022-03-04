"""In-memory entities repository."""

from typing import Dict, Optional
from uuid import UUID

from entities import Entity
from interface_adapters.repositories.base import (CardRepository, Repository,
                                                  TagRepository)


class InMemoryRepository(Repository):
    """
    Base class for in-memory repositories.

    The data is stored (privately) in a dictionary.
    """

    _data: Dict = {}

    @classmethod
    def save(cls, entity: Entity) -> None:
        """Persist a new entity."""
        cls._data[entity.id] = entity

    @classmethod
    def get(cls, id: UUID) -> Optional[Entity]:  # noqa: VNE003
        """Retrieve an entity by its id."""
        return cls._data.get(id)

    @classmethod
    def update(cls, id: UUID, **kwargs) -> None:  # noqa: VNE003
        """Update an entity and persist the changes."""
        entity = cls.get(id)

        if entity is not None:
            updated_entity = cls.entity(id=entity.id, **kwargs)

            cls.save(updated_entity)

    @classmethod
    def remove(cls, id: UUID) -> None:  # noqa: VNE003
        """Remove an entity and persist the changes."""
        entity = cls.get(id)

        if entity is not None:
            del cls._data[entity.id]

    @classmethod
    def list(cls) -> list[Entity]:
        """Retrieve a list of entities."""
        return list(cls._data.values())


class InMemoryTagRepository(InMemoryRepository, TagRepository):
    """In-memory repository for tags."""


class InMemoryCardRepository(InMemoryRepository, CardRepository):
    """In-memory repository for cards."""
