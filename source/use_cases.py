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


class UpdateTag(UseCase):
    """Implements the use case of updating a tag."""

    def execute(self, id, name):  # noqa: VNE003
        """Return a card from the repository."""
        return self._repository.update(id, name)


class DeleteTag(UseCase):
    """Implements the use of deleting a tag."""

    def execute(self, id):  # noqa: VNE003
        """Remove a tag from the repository."""
        self._repository.remove(id)


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


class UpdateCard(UseCase):
    """Implements the use case of updating a card."""

    def execute(self, id, text, tags):  # noqa: VNE003
        """Return a card from the repository."""
        return self._repository.update(id, text, tags)


class DeleteCard(UseCase):
    """Implements the use of deleting a card."""

    def execute(self, id):  # noqa: VNE003
        """Remove a card from the repository."""
        self._repository.remove(id)


class ListCards(UseCase):
    """Implements the use of listing cards, filtering by tags."""

    def execute(self, tags):
        """Return a card from the repository."""
        return self._repository.list(tags)
