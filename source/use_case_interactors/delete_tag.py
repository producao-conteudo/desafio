"""Delete tag use case interactor."""
from uuid import UUID

from use_case_interactors.base import TagUseCaseInteractor


class DeleteTag(TagUseCaseInteractor):
    """Use case of deleting a tag."""

    def execute(self, id: UUID) -> None:  # noqa: VNE003
        """Remove a tag from the repository."""
        self._repository.remove(id)
