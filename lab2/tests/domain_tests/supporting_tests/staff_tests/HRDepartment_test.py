import pytest
from core.enums.Permission import Permission
from core.exceptions import NotFoundError
from domain.processes.supporting.staff.HRDepartment import HRDepartment
from domain.processes.supporting.staff.EmailAccount import EmailAccount
from domain.processes.supporting.staff.Employee import Employee


def test_hire_employee(
    HR_department: HRDepartment, email_account: EmailAccount
) -> None:
    HR_department.hire_employee("John", "Doe", Permission.LEVEL_THREE, email_account)

    assert len(HR_department.employees) == 1
    assert HR_department.employees[0].id == 1


def test_fire_employee(
    HR_department: HRDepartment, email_account: EmailAccount
) -> None:
    HR_department.hire_employee("John", "Doe", Permission.LEVEL_THREE, email_account)

    HR_department.fire_employee(1)

    assert len(HR_department.employees) == 0


def test_fire_employee_with_not_found_error(
    HR_department: HRDepartment, email_account: EmailAccount
) -> None:
    HR_department.hire_employee("John", "Doe", Permission.LEVEL_THREE, email_account)

    with pytest.raises(NotFoundError):
        HR_department.fire_employee(2)


def test_change_employee_permission(
    employee: Employee, HR_department: HRDepartment
) -> None:
    HR_department.change_employee_permission(employee, Permission.LEVEL_FIVE)

    assert employee._permission == Permission.LEVEL_FIVE
