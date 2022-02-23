"""Domain's entities."""
from dataclasses import dataclass, field


@dataclass
class Tag:
    """Represents a tag."""

    text: str


@dataclass
class Card:
    """Represents a card."""

    text: str
    tags: list[Tag] = field(default_factory=list)
