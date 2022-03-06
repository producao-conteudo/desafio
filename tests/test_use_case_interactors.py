"""Unit tests for the application's use case interactors."""
from pytest_mock import MockerFixture
from use_case_interactors import (CreateCard, CreateTag, DeleteCard, DeleteTag,
                                  ListCards, ReadCard, ReadTag, UpdateCard,
                                  UpdateTag, UseCaseInteractor)


class BaseTest:
    """Base class for use case interactors' tests."""

    use_case_interactor: UseCaseInteractor

    def has_method(self, name: str) -> None:
        """Check if it has a specific method."""
        return callable(getattr(self.use_case_interactor, name, None))

    def test_init(self, mocker: MockerFixture) -> None:
        """Assert that it can be instantiated with arguments."""
        use_case_interactor = self.use_case_interactor()

        assert isinstance(use_case_interactor, self.use_case_interactor)

    def test_has_execute_method(self) -> None:
        """Assert that it has a method named 'execute'."""
        assert self.has_method('execute')


class TestCreateTag(BaseTest):
    """Unit tests for the CreateTag use case."""

    use_case_interactor = CreateTag

    def test_execute_method_calls_save_method_from_repository(
        self,
        mocker,
    ) -> None:
        """Assert that it calls the repository's save method."""
        use_case_interactor = self.use_case_interactor()
        use_case_interactor._repository = mocker.Mock()
        use_case_interactor.execute(name='test')

        use_case_interactor._repository.save.assert_called_once()


class TestReadTag(BaseTest):
    """Unit tests for the ReadTag use case."""

    use_case_interactor = ReadTag

    def test_execute_method_calls_get_method_from_repository(
        self,
        mocker: MockerFixture,
    ) -> None:
        """Assert that it calls the repository's get method."""
        use_case_interactor = self.use_case_interactor()
        use_case_interactor._repository = mocker.Mock()
        use_case_interactor.execute(id=None)

        use_case_interactor._repository.get.assert_called_once()


class TestUpdateTag(BaseTest):
    """Unit tests for the UpdateTag use case."""

    use_case_interactor = UpdateTag

    def test_execute_method_calls_update_method_from_repository(
        self,
        mocker: MockerFixture,
    ) -> None:
        """Assert that it calls the repository's update method."""
        use_case_interactor = self.use_case_interactor()
        use_case_interactor._repository = mocker.Mock()
        use_case_interactor.execute(id=None, name=None)

        use_case_interactor._repository.update.assert_called_once()


class TestDeleteTag(BaseTest):
    """Unit tests for the DeleteTag use case."""

    use_case_interactor = DeleteTag

    def test_execute_method_calls_remove_method_from_repository(
        self,
        mocker: MockerFixture,
    ) -> None:
        """Assert that it calls the repository's remove method."""
        use_case_interactor = self.use_case_interactor()
        use_case_interactor._repository = mocker.Mock()
        use_case_interactor.execute(id=None)

        use_case_interactor._repository.remove.assert_called_once()


class TestCreateCard(BaseTest):
    """Unit tests for the CreateCard use case."""

    use_case_interactor = CreateCard

    def test_execute_method_calls_save_method_from_repository(
        self,
        mocker: MockerFixture,
    ) -> None:
        """Assert that it calls the repository's save method."""
        use_case_interactor = self.use_case_interactor()
        use_case_interactor._repository = mocker.Mock()
        use_case_interactor.execute(text='test', tags=[])

        use_case_interactor._repository.save.assert_called_once()


class TestReadCard(BaseTest):
    """Unit tests for the ReadCard use case."""

    use_case_interactor = ReadCard

    def test_execute_method_calls_get_method_from_repository(
        self,
        mocker: MockerFixture,
    ) -> None:
        """Assert that it calls the repository's get method."""
        use_case_interactor = self.use_case_interactor()
        use_case_interactor._repository = mocker.Mock()
        use_case_interactor.execute(id=None)

        use_case_interactor._repository.get.assert_called_once()


class TestUpdateCard(BaseTest):
    """Unit tests for the UpdateCard use case."""

    use_case_interactor = UpdateCard

    def test_execute_method_calls_update_method_from_repository(
        self,
        mocker: MockerFixture,
    ) -> None:
        """Assert that it calls the repository's update method."""
        use_case_interactor = self.use_case_interactor()
        use_case_interactor._repository = mocker.Mock()
        use_case_interactor.execute(id=None, text=None, tags=[])

        use_case_interactor._repository.update.assert_called_once()


class TestDeleteCard(BaseTest):
    """Unit tests for the DeleteCard use case."""

    use_case_interactor = DeleteCard

    def test_execute_method_calls_remove_method_from_repository(
        self,
        mocker: MockerFixture,
    ) -> None:
        """Assert that it calls the repository's remove method."""
        use_case_interactor = self.use_case_interactor()
        use_case_interactor._repository = mocker.Mock()
        use_case_interactor.execute(id=None)

        use_case_interactor._repository.remove.assert_called_once()


class TestListCards(BaseTest):
    """Unit tests for the ListCards use case."""

    use_case_interactor = ListCards

    def test_execute_method_calls_list_method_from_repository(
        self,
        mocker: MockerFixture,
    ) -> None:
        """Assert that it calls the repository's list method."""
        use_case_interactor = self.use_case_interactor()
        use_case_interactor._repository = mocker.Mock()
        use_case_interactor.execute(tags=[])

        use_case_interactor._repository.list.assert_called_once()
