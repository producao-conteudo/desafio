"""Unit tests for the update card use case interactor."""
from pytest_mock import MockerFixture
from use_case_interactors.update_card import UpdateCard


def test_execute_method_calls_update_method_from_repository(
    mocker: MockerFixture,
) -> None:
    """Assert that it calls the repository's update method."""
    use_case_interactor = UpdateCard()
    use_case_interactor._repository = mocker.Mock()
    use_case_interactor.execute(id=None, text=None, tags=[])

    use_case_interactor._repository.update.assert_called_once()
