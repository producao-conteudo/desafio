"""Read card use case interactor."""
from typing import Optional
from uuid import UUID

from entities import Card
from use_case_interactors.base import CardUseCaseInteractor


class ReadCard(CardUseCaseInteractor):
    """Use case of reading a card."""

    def execute(self, id: UUID) -> Optional[Card]:  # noqa: VNE003
        """Return a card from the repository."""
        return self._repository.get(id)
