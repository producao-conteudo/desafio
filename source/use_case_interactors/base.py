"""Abstract base use case interactors."""
from abc import ABC, abstractmethod
from typing import Any, Optional

from interface_adapters.repositories import Repository
from settings import CARD_REPOSITORY, TAG_REPOSITORY


class UseCaseInteractor(ABC):
    """Base class for all use case interactors."""

    def __init__(self, repository: Repository):
        self._repository = repository

    @abstractmethod
    def execute(self) -> Optional[Any]:
        """Execute use case's business logic."""


class TagUseCaseInteractor(UseCaseInteractor):
    """Base class for tag use case interactors."""

    def __init__(self):
        super().__init__(repository=TAG_REPOSITORY)


class CardUseCaseInteractor(UseCaseInteractor):
    """Base class for card use case interactors."""

    def __init__(self):
        super().__init__(repository=CARD_REPOSITORY)
