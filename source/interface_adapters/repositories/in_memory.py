"""In-memory entities repository."""

from interface_adapters.repositories.base import (CardRepository, Repository,
                                                  TagRepository)


class InMemoryRepository(Repository):
    """
    Base class for in-memory repositories.

    The data is stored (privately) as a dictionary.
    """

    _data = {}

    @classmethod
    def save(cls, entity):
        """Persist a new entity."""
        cls._data[entity.id] = entity

    @classmethod
    def get(cls, id):  # noqa: VNE003
        """Retrieve an entity by its id."""
        return cls._data.get(id)

    @classmethod
    def update(cls, id, **kwargs):  # noqa: VNE003
        """Update an entity and persist the changes."""
        entity = cls.get(id)

        if entity is not None:
            updated_entity = cls.entity(id=entity.id, **kwargs)

            cls.save(updated_entity)

    @classmethod
    def remove(cls, id):  # noqa: VNE003
        """Remove an entity and persist the changes."""
        entity = cls.get(id)

        if entity is not None:
            del cls._data[entity.id]

    @classmethod
    def list(cls):
        """Retrieve a list of entities."""
        return list(cls._data.values())


class InMemoryTagRepository(InMemoryRepository, TagRepository):
    """In-memory repository for tags."""


class InMemoryCardRepository(InMemoryRepository, CardRepository):
    """In-memory repository for cards."""
