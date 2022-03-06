"""Settings module."""
from interface_adapters.repositories import (InMemoryCardRepository,
                                             InMemoryTagRepository)

# Repositories
CARD_REPOSITORY = InMemoryCardRepository
TAG_REPOSITORY = InMemoryTagRepository
