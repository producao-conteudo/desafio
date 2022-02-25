"""Application's use cases."""
from abc import ABC, abstractmethod

from entities import Card, Tag


class UseCase(ABC):
    """Base class for use cases."""

    def __init__(self, repository):
        self._repository = repository

    @abstractmethod
    def execute(self):
        """Implement call to repository method."""


class CreateTag(UseCase):
    """Implements the use of creating a new tag."""

    def execute(self, name):
        """Create a new tag and persist it in the repository."""
        tag = Tag(name=name)

        self._repository.save(tag)


class ReadTag(UseCase):
    """Implements the use of creating a new tag."""

    def execute(self, id):  # noqa: VNE003
        """Return a tag from the repository."""
        return self._repository.get(id)


class CreateCard(UseCase):
    """Implements the use of creating a new card."""

    def execute(self, text, tags):
        """Create a new card and persist it in the repository."""
        card = Card(text=text, tags=tags)

        self._repository.save(card)


class ReadCard(UseCase):
    """Implements the use of reading a card."""

    def execute(self, id):  # noqa: VNE003
        """Return a card from the repository."""
        return self._repository.get(id)


class ListCards(UseCase):
    """Implements the use of listing cards filtering by tags."""

    def execute(self, tags):
        """Return a card from the repository."""
        return self._repository.list(tags)
