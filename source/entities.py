"""Domain's entities."""
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class Tag:
    """Represents a tag."""

    name: str
    id: UUID = field(default_factory=uuid4)  # noqa: VNE003


@dataclass
class Card:
    """Represents a card."""

    text: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    tags: list[Tag] = field(default_factory=list)
    id: UUID = field(default_factory=uuid4)  # noqa: VNE003
