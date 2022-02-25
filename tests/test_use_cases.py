"""Unit tests for the application's use cases."""
from pytest import raises
from use_cases import CreateCard, CreateTag, ListCards, ReadCard, ReadTag


class BaseTest:
    """Base class for use cases' tests."""

    use_case = None

    def has_method(self, name):
        """Check if it has a specific method."""
        return callable(getattr(self.use_case, name, None))

    def test_init_without_arguments(self):
        """Assert that it can't be instantiated without arguments."""
        with raises(TypeError) as _:
            self.use_case()

    def test_init_with_arguments(self, mocker):
        """Assert that it can be instantiated with arguments."""
        use_case = self.use_case(repository=mocker.Mock())

        assert isinstance(use_case, self.use_case)

    def test_has_execute_method(self):
        """Assert that it has a method named 'execute'."""
        assert self.has_method('execute')


class TestCreateTag(BaseTest):
    """Unit tests for the CreateTag use case."""

    use_case = CreateTag

    def test_execute_method_calls_save_method_from_repository(self, mocker):
        """Assert that it calls the repository's save method."""
        repository = mocker.Mock()

        use_case = self.use_case(repository=repository)
        use_case.execute(name='test')

        repository.save.assert_called_once()


class TestReadTag(BaseTest):
    """Unit tests for the ReadTag use case."""

    use_case = ReadTag

    def test_execute_method_calls_get_method_from_repository(self, mocker):
        """Assert that it calls the repository's get method."""
        repository = mocker.Mock()

        use_case = self.use_case(repository=repository)
        use_case.execute(id=None)

        repository.get.assert_called_once()


class TestCreateCard(BaseTest):
    """Unit tests for the CreateCard use case."""

    use_case = CreateCard

    def test_execute_method_calls_save_method_from_repository(self, mocker):
        """Assert that it calls the repository's save method."""
        repository = mocker.Mock()

        use_case = self.use_case(repository=repository)
        use_case.execute(text='test', tags=[])

        repository.save.assert_called_once()


class TestReadCard(BaseTest):
    """Unit tests for the ReadCard use case."""

    use_case = ReadCard

    def test_execute_method_calls_get_method_from_repository(self, mocker):
        """Assert that it calls the repository's get method."""
        repository = mocker.Mock()

        use_case = self.use_case(repository=repository)
        use_case.execute(id=None)

        repository.get.assert_called_once()


class TestListCards(BaseTest):
    """Unit tests for the ReadCard use case."""

    use_case = ListCards

    def test_execute_method_calls_list_method_from_repository(self, mocker):
        """Assert that it calls the repository's list method."""
        repository = mocker.Mock()

        use_case = self.use_case(repository=repository)
        use_case.execute(tags=[])

        repository.list.assert_called_once()
