import pytest
from core.enums.status import Status
from core.exceptions import NotFoundError
from domain.processes.supporting.staff.employee import Employee
from domain.processes.supporting.staff.employee_task import EmployeeTask


def test_assing_task(employee: Employee, task: EmployeeTask) -> None:
    employee.assing_task(task)

    assert employee._task_list[0]._description == "bbb"
    assert task._status == Status.IN_PROCCES


def test_complete_task(employee: Employee, task: EmployeeTask) -> None:
    employee.assing_task(task)

    employee.complete_task(task._id)

    assert task._status == Status.COMPLITED


def test_complete_task_with_error(employee: Employee) -> None:
    with pytest.raises(NotFoundError):
        employee.complete_task("bbb")
