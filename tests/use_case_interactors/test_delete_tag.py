"""Unit tests for the delete tag use case interactor."""
from pytest_mock import MockerFixture
from use_case_interactors.delete_tag import DeleteTag


def test_execute_method_calls_remove_method_from_repository(
    mocker: MockerFixture,
) -> None:
    """Assert that it calls the repository's remove method."""
    use_case_interactor = DeleteTag()
    use_case_interactor._repository = mocker.Mock()
    use_case_interactor.execute(id=None)

    use_case_interactor._repository.remove.assert_called_once()
