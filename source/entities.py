"""Domain's entities."""
from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(kw_only=True)
class Entity(ABC):
    """Represents a entity from the domain."""

    id: UUID = field(default_factory=uuid4)  # noqa: VNE003


@dataclass
class Tag(Entity):
    """Represents a tag entity."""

    name: str


@dataclass
class Card(Entity):
    """Represents a card entity."""

    text: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    tags: list[Tag] = field(default_factory=list)
