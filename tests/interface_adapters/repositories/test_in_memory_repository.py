"""Unit tests for the in-memory repository."""
from entities import Entity
from interface_adapters.repositories import InMemoryRepository
from pytest import fixture


@fixture
def entity() -> Entity:
    """Return an entity."""
    return Entity()


@fixture
def repository(entity) -> InMemoryRepository:
    """Return the in-memory repository."""
    repository = InMemoryRepository()
    repository._data[entity.id] = entity

    return repository


def test_save_method(repository: InMemoryRepository) -> None:
    """Assert that it saves an entity correctly."""
    entity = Entity()
    repository.save(entity)

    assert entity.id in repository._data


def test_get_method(repository: InMemoryRepository, entity: Entity) -> None:
    """Assert that it retrieves an entity correctly."""
    assert entity == repository.get(entity.id)


def test_update_method(repository: InMemoryRepository, entity: Entity) -> None:
    """Assert that it updates an entity correctly."""
    kwargs = {}
    repository.update(id=entity.id, **kwargs)

    assert entity == repository.get(entity.id)


def test_remove_method(repository: InMemoryRepository, entity: Entity) -> None:
    """Assert that it removes an entity correctly."""
    repository.remove(entity.id)

    assert repository.get(entity.id) is None


def test_list_method(repository: InMemoryRepository) -> None:
    """Assert that it lists all entities correctly."""
    assert isinstance(repository.list(), list)
