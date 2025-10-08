from task1.bubble_sort import bubble_sort
from task1.tests.user_class import UserClass


def test_bubble_sort_with_int(nums: list[int], sorted_nums: list[int]) -> None:
    bubble_sort(nums)
    assert nums == sorted_nums


def test_bubble_sort_with_str(strings: list[str], sorted_strings: list[str]) -> None:
    bubble_sort(strings)
    assert strings == sorted_strings


def test_bubble_sort_with_user_class(
    user_classes: list[UserClass], sorted_user_classes: list[UserClass]
) -> None:
    bubble_sort(user_classes)
    assert user_classes == sorted_user_classes
