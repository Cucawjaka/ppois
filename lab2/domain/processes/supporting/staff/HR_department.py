from core.exceptions import NotFoundError
from core.utils.id_generator import IDGenerator
from domain.processes.supporting.staff.email_account import EmailAccount
from domain.processes.supporting.staff.employee import Employee
from core.enums.permission import Permission


class HRDepartment:
    def __init__(self, id_generator: IDGenerator) -> None:
        self.employees: list[Employee] = list()
        self.id_generator: IDGenerator = id_generator

    def hire_employee(
        self,
        first_name: str,
        last_name: str,
        permission: Permission,
        email: EmailAccount,
    ) -> Employee:
        new_employee: Employee = Employee(
            self.id_generator.create_int_id(), first_name, last_name, permission, email
        )

        self.employees.append(new_employee)
        return new_employee

    def fire_employee(self, employee_id: int) -> None:
        for employee in self.employees:
            if employee.id == employee_id:
                self.employees.remove(employee)
                break
        else:
            raise NotFoundError(f"Сотрудник с id {employee_id} не найдем")

    def change_employee_permission(
        self, employee: Employee, new_permission: Permission
    ) -> None:
        employee.set_permission(new_permission)
