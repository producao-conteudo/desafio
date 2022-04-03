"""Delete card use case interactor."""
from uuid import UUID

from use_case_interactors.base import CardUseCaseInteractor


class DeleteCard(CardUseCaseInteractor):
    """Use case of deleting a card."""

    def execute(self, id: UUID) -> None:  # noqa: VNE003
        """Remove a card from the repository."""
        self._repository.remove(id)
