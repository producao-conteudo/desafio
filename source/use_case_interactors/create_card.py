"""Create card use case interactor."""
from entities import Card, Tag
from use_case_interactors.base import CardUseCaseInteractor


class CreateCard(CardUseCaseInteractor):
    """Use case of creating a new card."""

    def execute(self, text: str, tags: list[Tag]) -> None:
        """Create a new card and persist it in the repository."""
        card = Card(text=text, tags=tags)

        self._repository.save(card)
