import pytest

from task1.tests.UserClass import UserClass


@pytest.fixture(scope="session")
def nums() -> list[int]:
    return [5, 7, 4, 9, 3, 5]


@pytest.fixture(scope="session")
def sorted_nums() -> list[int]:
    return [3, 4, 5, 5, 7, 9]


@pytest.fixture(scope="session")
def strings() -> list[str]:
    return ["da", "d", "ba", "c", "bb"]


@pytest.fixture(scope="session")
def sorted_strings() -> list[str]:
    return ["ba", "bb", "c", "d", "da"]


@pytest.fixture(scope="session")
def user_classes() -> list[UserClass]:
    return [
        UserClass(5),
        UserClass(7),
        UserClass(4),
        UserClass(9),
        UserClass(3),
        UserClass(5),
    ]


@pytest.fixture(scope="session")
def sorted_user_classes() -> list[UserClass]:
    return [
        UserClass(3),
        UserClass(4),
        UserClass(5),
        UserClass(5),
        UserClass(7),
        UserClass(9),
    ]
