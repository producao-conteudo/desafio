"""Unit tests for the base repository."""
from abc import ABCMeta

from interface_adapters.repositories import Repository


def has_method(name: str) -> bool:
    """Check if it has a specific method."""
    return callable(getattr(Repository, name, None))


def test_is_abstract() -> None:
    """Assert that it is an abstract base class (ABC)."""
    assert isinstance(Repository, ABCMeta)


def test_has_save_method() -> None:
    """Assert that it has a method named 'save'."""
    assert has_method('save')


def test_save_method_is_abstract() -> None:
    """Assert that save is an abstractmethod."""
    assert Repository.save.__isabstractmethod__


def test_has_get_method() -> None:
    """Assert that it has a method named 'get'."""
    assert has_method('get')


def test_get_method_is_abstract() -> None:
    """Assert that get is an abstractmethod."""
    assert Repository.get.__isabstractmethod__


def test_has_update_method() -> None:
    """Assert that it has a method named 'update'."""
    assert has_method('update')


def test_update_method_is_abstract() -> None:
    """Assert that update is an abstractmethod."""
    assert Repository.update.__isabstractmethod__


def test_has_remove_method() -> None:
    """Assert that it has a method named 'remove'."""
    assert has_method('remove')


def test_remove_method_is_abstract() -> None:
    """Assert that remove is an abstractmethod."""
    assert Repository.remove.__isabstractmethod__
