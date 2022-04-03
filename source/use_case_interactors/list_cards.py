"""List cards use case interactor."""
from entities import Card, Tag
from use_case_interactors.base import CardUseCaseInteractor


class ListCards(CardUseCaseInteractor):
    """Use case of listing cards, filtering by tags."""

    def execute(self, tags: list[Tag]) -> list[Card]:
        """Return a list of cards from the repository, filtering by tags."""
        return self._repository.list(tags)
