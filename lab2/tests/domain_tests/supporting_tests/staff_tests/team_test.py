import pytest
from core.exceptions import NotFoundError
from domain.processes.supporting.staff.employee import Employee
from domain.processes.supporting.staff.team import Team


def test_add_member(team: Team, employee: Employee) -> None:
    team.add_member(employee)

    assert len(team._employee_list) == 2
    assert team._employee_list[1].id == 1


def test_remove_member(team: Team) -> None:
    team.remove_member(2)

    assert len(team._employee_list) == 0


def test_remove_member_with_exception(team: Team) -> None:
    with pytest.raises(NotFoundError):
        team.remove_member(4)


def test_assign_manager(team: Team, employee: Employee) -> None:
    team.assing_manager(employee)

    assert team._manager.id == 1
