"""Unit tests for the domain's entities."""

from dataclasses import dataclass, fields, is_dataclass
from datetime import datetime
from uuid import UUID

from entities import Card, Tag
from pytest import fixture


class BaseTest:
    """Base class for entities' tests."""

    entity: dataclass = None

    def has_field(self, name):
        """Check if it has a specific field."""
        return any(field.name == name for field in fields(self.entity))

    def field_type(self, name):
        """Return the type of a specific field."""
        field = [
            field for field in fields(self.entity) if field.name == name
        ].pop(0)

        return field.type

    def test_is_dataclass(self):
        """Assert that it is a dataclass."""
        assert is_dataclass(self.entity)


class TestTag(BaseTest):
    """Unit tests for the Tag entity."""

    entity = Tag

    @fixture
    def name(self):
        """Return a tag name."""
        return 'test tag name'

    def test_init(self, name):
        """Assert that it can be instantiated."""
        tag = self.entity(name=name)

        assert isinstance(tag, self.entity)

    def test_has_name_field(self):
        """Assert that it has a field named 'name'."""
        assert self.has_field('name')

    def test_name_field_type_is_str(self):
        """Assert that the name field's type is str."""
        assert self.field_type('name') == str


class TestCard(BaseTest):
    """Unit tests for the Card entity."""

    entity = Card

    @fixture
    def text(self):
        """Return a card text."""
        return 'card text test'

    def test_init(self, text):
        """Assert that it can be instantiated."""
        card = self.entity(text=text)

        assert isinstance(card, self.entity)

    def test_has_text_field(self):
        """Assert that it has a field named 'text'."""
        assert self.has_field('text')

    def test_has_created_at_field(self):
        """Assert that it has a field named 'created_at'."""
        assert self.has_field('created_at')

    def test_created_at_field_type_is_datetime(self):
        """Assert that the created_at field's type is datetime."""
        assert self.field_type('created_at') == datetime

    def test_text_field_type_is_str(self):
        """Assert that the text field's type is str."""
        assert self.field_type('text') == str

    def test_has_tags_field(self):
        """Assert that it has a field named 'tags'."""
        assert self.has_field('tags')

    def test_tags_field_type_is_list_of_tag(self):
        """Assert that the text field's type is list of Tag entities."""
        assert self.field_type('tags') == list[Tag]

    def test_has_id_field(self):
        """Assert that it has a field named 'id'."""
        assert self.has_field('id')

    def test_id_field_type_is_uuid(self):
        """Assert that the id field's type is list of Tag entities."""
        assert self.field_type('id') == UUID
