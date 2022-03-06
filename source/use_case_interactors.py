"""Application's use case interactors."""
from abc import ABC, abstractmethod
from typing import Any, Optional
from uuid import UUID

from entities import Card, Tag
from interface_adapters.repositories import Repository
from settings import CARD_REPOSITORY, TAG_REPOSITORY


class UseCaseInteractor(ABC):
    """Base class for use case interactors."""

    def __init__(self, repository: Repository):
        self._repository = repository

    @abstractmethod
    def execute(self) -> Optional[Any]:
        """Call repository's method."""


class TagUseCaseInteractor(UseCaseInteractor):
    """Base class for tag use case interactors."""

    def __init__(self):
        super().__init__(repository=TAG_REPOSITORY)


class CreateTag(TagUseCaseInteractor):
    """Use case of creating a new tag."""

    def execute(self, name: str) -> None:
        """Create a new tag and persist it in the repository."""
        tag = Tag(name=name)

        self._repository.save(tag)


class ReadTag(TagUseCaseInteractor):
    """Use case of reading a tag."""

    def execute(self, id: UUID) -> Optional[Tag]:  # noqa: VNE003
        """Return a tag from the repository."""
        return self._repository.get(id)


class UpdateTag(TagUseCaseInteractor):
    """Use case of updating a tag."""

    def execute(self, id: UUID, name: str) -> None:  # noqa: VNE003
        """Return a card from the repository."""
        self._repository.update(id, name)


class DeleteTag(TagUseCaseInteractor):
    """Use case of deleting a tag."""

    def execute(self, id: UUID) -> None:  # noqa: VNE003
        """Remove a tag from the repository."""
        self._repository.remove(id)


class CardUseCaseInteractor(UseCaseInteractor):
    """Base class for card use case interactors."""

    def __init__(self):
        super().__init__(repository=CARD_REPOSITORY)


class CreateCard(CardUseCaseInteractor):
    """Use case of creating a new card."""

    def execute(self, text: str, tags: list[Tag]) -> None:
        """Create a new card and persist it in the repository."""
        card = Card(text=text, tags=tags)

        self._repository.save(card)


class ReadCard(CardUseCaseInteractor):
    """Use case of reading a card."""

    def execute(self, id: UUID) -> Optional[Card]:  # noqa: VNE003
        """Return a card from the repository."""
        return self._repository.get(id)


class UpdateCard(CardUseCaseInteractor):
    """Use case of updating a card."""

    def execute(
        self,
        id: UUID,  # noqa: VNE003
        text: str,
        tags: list[Tag],
    ) -> None:
        """Return a card from the repository."""
        self._repository.update(id, text, tags)


class DeleteCard(CardUseCaseInteractor):
    """Use case of deleting a card."""

    def execute(self, id: UUID) -> None:  # noqa: VNE003
        """Remove a card from the repository."""
        self._repository.remove(id)


class ListCards(CardUseCaseInteractor):
    """Use case of listing cards, filtering by tags."""

    def execute(self, tags: list[Tag]) -> list[Card]:
        """Return a list of cards from the repository, filtering by tags."""
        return self._repository.list(tags)
