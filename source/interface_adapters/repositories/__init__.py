"""Data access interface adapters."""
from interface_adapters.repositories.base import Repository
from interface_adapters.repositories.in_memory import (InMemoryCardRepository,
                                                       InMemoryRepository,
                                                       InMemoryTagRepository)

__all__ = (
    'Repository',
    'InMemoryCardRepository',
    'InMemoryRepository',
    'InMemoryTagRepository',
)
