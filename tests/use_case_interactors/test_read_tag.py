"""Unit tests for the read tag use case interactor."""
from pytest_mock import MockerFixture
from use_case_interactors.read_tag import ReadTag


def test_execute_method_calls_get_method_from_repository(
    mocker: MockerFixture,
) -> None:
    """Assert that it calls the repository's get method."""
    use_case_interactor = ReadTag()
    use_case_interactor._repository = mocker.Mock()
    use_case_interactor.execute(id=None)

    use_case_interactor._repository.get.assert_called_once()
