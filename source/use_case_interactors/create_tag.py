"""Create tag use case interactor."""
from entities import Tag
from use_case_interactors.base import TagUseCaseInteractor


class CreateTag(TagUseCaseInteractor):
    """Use case of creating a new tag."""

    def execute(self, name: str) -> None:
        """Create a new tag and persist it in the repository."""
        tag = Tag(name=name)

        self._repository.save(tag)
