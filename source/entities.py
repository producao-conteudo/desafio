"""Domain's entities."""
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(kw_only=True, unsafe_hash=True)
class Entity:
    """Base class for domain's entities."""

    id: UUID = field(default_factory=uuid4)  # noqa: VNE003


@dataclass
class Tag(Entity):
    """Tag entity."""

    name: str


@dataclass
class Card(Entity):
    """Card entity."""

    text: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    tags: list[Tag] = field(default_factory=list)
