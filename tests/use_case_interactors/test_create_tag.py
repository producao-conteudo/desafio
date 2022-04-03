"""Unit tests for the create tag use case interactor."""
from pytest_mock import MockerFixture
from use_case_interactors.create_tag import CreateTag


def test_execute_method_calls_save_method_from_repository(
    mocker: MockerFixture,
) -> None:
    """Assert that it calls the repository's save method."""
    use_case_interactor = CreateTag()
    use_case_interactor._repository = mocker.Mock()
    use_case_interactor.execute(name='test')

    use_case_interactor._repository.save.assert_called_once()
