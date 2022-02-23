"""Domain's entities."""
from dataclasses import dataclass


@dataclass
class Tag:
    """Represents a tag."""

    text: str


@dataclass
class Card:
    """Represents a card."""

    text: str
