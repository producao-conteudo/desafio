"""Unit tests for the update tag use case interactor."""
from pytest_mock import MockerFixture
from use_case_interactors.update_tag import UpdateTag


def test_execute_method_calls_update_method_from_repository(
    mocker: MockerFixture,
) -> None:
    """Assert that it calls the repository's update method."""
    use_case_interactor = UpdateTag()
    use_case_interactor._repository = mocker.Mock()
    use_case_interactor.execute(id=None, name=None)

    use_case_interactor._repository.update.assert_called_once()
