"""Read tag use case interactor."""
from typing import Optional
from uuid import UUID

from entities import Tag
from use_case_interactors.base import TagUseCaseInteractor


class ReadTag(TagUseCaseInteractor):
    """Use case of reading a tag."""

    def execute(self, id: UUID) -> Optional[Tag]:  # noqa: VNE003
        """Return a tag from the repository."""
        return self._repository.get(id)
