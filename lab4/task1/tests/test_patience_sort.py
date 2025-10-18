from task1.patience_sort import patience_sort
from task1.tests.UserClass import UserClass


def test_bubble_sort_with_int(nums: list[int], sorted_nums: list[int]) -> None:
    assert patience_sort(nums) == sorted_nums


def test_bubble_sort_with_str(strings: list[str], sorted_strings: list[str]) -> None:
    assert patience_sort(strings) == sorted_strings


def test_bubble_sort_with_user_class(
    user_classes: list[UserClass], sorted_user_classes: list[UserClass]
) -> None:
    assert patience_sort(user_classes) == sorted_user_classes
