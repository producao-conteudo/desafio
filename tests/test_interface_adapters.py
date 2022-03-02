"""Unit tests for the data access interface adapters."""
from abc import ABCMeta

from entities import Entity
from interface_adapters import InMemoryRepository, Repository
from pytest import fixture


class TestRepository:
    """Unit tests for the repository interface adapter."""

    def has_method(self, name):
        """Check if it has a specific method."""
        return callable(getattr(Repository, name, None))

    def test_is_abstract(self):
        """Assert that it is an abstract base class (ABC)."""
        assert isinstance(Repository, ABCMeta)

    def test_has_save_method(self):
        """Assert that it has a method named 'save'."""
        assert self.has_method('save')

    def test_save_method_is_abstract(self):
        """Assert that save is an abstractmethod."""
        assert Repository.save.__isabstractmethod__

    def test_has_get_method(self):
        """Assert that it has a method named 'get'."""
        assert self.has_method('get')

    def test_get_method_is_abstract(self):
        """Assert that get is an abstractmethod."""
        assert Repository.get.__isabstractmethod__

    def test_has_update_method(self):
        """Assert that it has a method named 'update'."""
        assert self.has_method('update')

    def test_update_method_is_abstract(self):
        """Assert that update is an abstractmethod."""
        assert Repository.update.__isabstractmethod__

    def test_has_remove_method(self):
        """Assert that it has a method named 'remove'."""
        assert self.has_method('remove')

    def test_remove_method_is_abstract(self):
        """Assert that remove is an abstractmethod."""
        assert Repository.remove.__isabstractmethod__


class TestInMemoryRepository:
    """Unit tests for the in-memory repository."""

    @fixture
    def entity(self):
        """Return an entity."""
        return Entity()

    @fixture
    def repository(self, entity):
        """Return the in-memory repository."""
        repository = InMemoryRepository()
        repository._data[entity.id] = entity

        return repository

    def test_save_method(self, repository):
        """Assert that it saves an entity correctly."""
        entity = Entity()
        repository.save(entity)

        assert entity.id in repository._data

    def test_get_method(self, repository, entity):
        """Assert that it retrieves an entity correctly."""
        assert entity == repository.get(entity.id)

    def test_update_method(self, repository, entity):
        """Assert that it updates an entity correctly."""
        kwargs = {}
        repository.update(id=entity.id, **kwargs)

        assert entity == repository.get(entity.id)

    def test_remove_method(self, repository, entity):
        """Assert that it removes an entity correctly."""
        repository.remove(entity.id)

        assert repository.get(entity.id) is None

    def test_list_method(self, repository):
        """Assert that it lists all entities correctly."""
        assert isinstance(repository.list(), list)
