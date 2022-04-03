"""Update card use case interactor."""
from uuid import UUID

from entities import Tag
from use_case_interactors.base import CardUseCaseInteractor


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
