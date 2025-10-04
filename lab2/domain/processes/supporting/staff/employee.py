from core.exceptions import NotFoundError
from domain.processes.supporting.staff.email_account import EmailAccount
from domain.processes.supporting.staff.employee_task import EmployeeTask
from core.enums.permission import Permission


class Employee:
    def __init__(
        self,
        id: int,
        first_name: str,
        last_name: str,
        permission: Permission,
        email: EmailAccount,
    ) -> None:
        self._id: int = id
        self._first_name: str = first_name
        self._last_name: str = last_name
        self._email_account: EmailAccount = email
        self._permission: Permission = permission
        self._task_list: list[EmployeeTask] = list()

    @property
    def id(self) -> int:
        return self._id

    def set_permission(self, new_permission: Permission) -> None:
        self._permission = new_permission

    def assing_task(self, task: EmployeeTask) -> None:
        self._task_list.append(task)
        task.start()

    def complete_task(self, task_id: str) -> None:
        for task in self._task_list:
            if task.id == task_id:
                task.finish()
                break
        else:
            raise NotFoundError(f"Задача с id {task_id} не найдена")
