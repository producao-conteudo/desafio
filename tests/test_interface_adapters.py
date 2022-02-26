"""Unit tests for the data access interface adapters."""
from abc import ABCMeta

from interface_adapters import CardRepository, TagRepository


class TestTagRepository:
    """Unit tests for the tag repository."""

    repository = TagRepository

    def has_method(self, name):
        """Check if it has a specific method."""
        return callable(getattr(self.repository, name, None))

    def test_is_abstract(self):
        """Assert that it is an abstract base class (ABC)."""
        assert isinstance(self.repository, ABCMeta)

    def test_has_save_method(self):
        """Assert that it has a method named 'save'."""
        assert self.has_method('save')

    def test_save_method_is_abstract(self):
        """Assert that save is an abstractmethod."""
        assert self.repository.save.__isabstractmethod__

    def test_has_get_method(self):
        """Assert that it has a method named 'get'."""
        assert self.has_method('get')

    def test_get_method_is_abstract(self):
        """Assert that get is an abstractmethod."""
        assert self.repository.get.__isabstractmethod__

    def test_has_update_method(self):
        """Assert that it has a method named 'update'."""
        assert self.has_method('update')

    def test_update_method_is_abstract(self):
        """Assert that update is an abstractmethod."""
        assert self.repository.update.__isabstractmethod__

    def test_has_remove_method(self):
        """Assert that it has a method named 'remove'."""
        assert self.has_method('remove')

    def test_remove_method_is_abstract(self):
        """Assert that remove is an abstractmethod."""
        assert self.repository.remove.__isabstractmethod__


class TestCardRepository:
    """Unit tests for the card repository."""

    repository = CardRepository

    def has_method(self, name):
        """Check if it has a specific method."""
        return callable(getattr(self.repository, name, None))

    def test_is_abstract(self):
        """Assert that it is an abstract base class (ABC)."""
        assert isinstance(self.repository, ABCMeta)

    def test_has_save_method(self):
        """Assert that it has a method named 'save'."""
        assert self.has_method('save')

    def test_save_method_is_abstract(self):
        """Assert that save is an abstractmethod."""
        assert self.repository.save.__isabstractmethod__

    def test_has_get_method(self):
        """Assert that it has a method named 'get'."""
        assert self.has_method('get')

    def test_get_method_is_abstract(self):
        """Assert that get is an abstractmethod."""
        assert self.repository.get.__isabstractmethod__

    def test_has_update_method(self):
        """Assert that it has a method named 'update'."""
        assert self.has_method('update')

    def test_update_method_is_abstract(self):
        """Assert that update is an abstractmethod."""
        assert self.repository.update.__isabstractmethod__

    def test_has_remove_method(self):
        """Assert that it has a method named 'remove'."""
        assert self.has_method('remove')

    def test_remove_method_is_abstract(self):
        """Assert that remove is an abstractmethod."""
        assert self.repository.remove.__isabstractmethod__

    def test_has_list_method(self):
        """Assert that it has a method named 'list'."""
        assert self.has_method('list')

    def test_list_method_is_abstract(self):
        """Assert that list is an abstractmethod."""
        assert self.repository.list.__isabstractmethod__
