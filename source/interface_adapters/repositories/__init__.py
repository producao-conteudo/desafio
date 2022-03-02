"""Data access interface adapters."""
from interface_adapters.repositories.base import Repository
from interface_adapters.repositories.in_memory import InMemoryRepository

__all__ = (
    'Repository',
    'InMemoryRepository',
)
