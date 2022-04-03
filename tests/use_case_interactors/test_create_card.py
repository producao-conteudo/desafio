"""Unit tests for the create card use case interactor."""
from pytest_mock import MockerFixture
from use_case_interactors.create_card import CreateCard


def test_execute_method_calls_save_method_from_repository(
    mocker: MockerFixture,
) -> None:
    """Assert that it calls the repository's save method."""
    use_case_interactor = CreateCard()
    use_case_interactor._repository = mocker.Mock()
    use_case_interactor.execute(text='test', tags=[])

    use_case_interactor._repository.save.assert_called_once()
