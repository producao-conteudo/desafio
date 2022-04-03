"""Unit tests for the list cards use case interactor."""
from pytest_mock import MockerFixture
from use_case_interactors.list_cards import ListCards


def test_execute_method_calls_list_method_from_repository(
    mocker: MockerFixture,
) -> None:
    """Assert that it calls the repository's list method."""
    use_case_interactor = ListCards()
    use_case_interactor._repository = mocker.Mock()
    use_case_interactor.execute(tags=[])

    use_case_interactor._repository.list.assert_called_once()
