from core.exceptions import NotFoundError
from domain.processes.supporting.staff.employee import Employee


class Team:
    def __init__(self, id: str, manager: Employee) -> None:
        self._id = id
        self._employee_list: list[Employee] = [manager]
        self._manager: Employee = manager

    def add_member(self, employee: Employee) -> None:
        self._employee_list.append(employee)

    def remove_member(self, employee_id: int) -> None:
        for employee in self._employee_list:
            if employee.id == employee_id:
                self._employee_list.remove(employee)
                break
        else:
            raise NotFoundError(f"Работник с id {employee_id} не найден")

    def assing_manager(self, new_manager: Employee) -> None:
        self.add_member(new_manager)
        self._manager = new_manager
