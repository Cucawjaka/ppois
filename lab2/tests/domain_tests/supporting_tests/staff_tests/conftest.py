import pytest

from core.enums.permission import Permission
from core.utils.id_generator import IDGenerator
from domain.processes.supporting.staff.HR_department import HRDepartment
from domain.processes.supporting.staff.email_account import EmailAccount
from domain.processes.supporting.staff.employee import Employee
from domain.processes.supporting.staff.employee_task import EmployeeTask
from domain.processes.supporting.staff.team import Team


@pytest.fixture
def email_account() -> EmailAccount:
    return EmailAccount("john@gmail.com")


@pytest.fixture
def employee(email_account: EmailAccount) -> Employee:
    return Employee(1, "John", "Doe", Permission.LEVEL_THREE, email_account)


@pytest.fixture
def HR_department() -> HRDepartment:
    return HRDepartment(IDGenerator())


@pytest.fixture
def team() -> Team:
    manager_email: EmailAccount = EmailAccount("manager@gmail.com")
    manager: Employee = Employee(
        2, "very", "important", Permission.LEVEL_FIVE, manager_email
    )

    return Team("id", manager)


@pytest.fixture
def task() -> EmployeeTask:
    return EmployeeTask("bbb")
