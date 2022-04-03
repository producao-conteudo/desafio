"""Unit tests for the read card use case interactor."""
from pytest_mock import MockerFixture
from use_case_interactors.read_card import ReadCard


def test_execute_method_calls_get_method_from_repository(
    mocker: MockerFixture,
) -> None:
    """Assert that it calls the repository's get method."""
    use_case_interactor = ReadCard()
    use_case_interactor._repository = mocker.Mock()
    use_case_interactor.execute(id=None)

    use_case_interactor._repository.get.assert_called_once()
