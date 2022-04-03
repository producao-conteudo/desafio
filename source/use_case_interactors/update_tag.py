"""Update tag use case interactor."""
from uuid import UUID

from use_case_interactors.base import TagUseCaseInteractor


class UpdateTag(TagUseCaseInteractor):
    """Use case of updating a tag."""

    def execute(self, id: UUID, name: str) -> None:  # noqa: VNE003
        """Return a card from the repository."""
        self._repository.update(id, name)
