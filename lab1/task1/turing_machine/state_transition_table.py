from turing_machine.transition import Transition


class StateTransitionTable:
    """Устройство управления"""
    def __init__(self) -> None:
        self._table: dict[str, dict[str, Transition]] = {}
        self._current_state: str = ""
        

    def add_state(
            self,
            transition: Transition,
            letter: str,
            state_name: str
            ) -> None:
        if state_name not in self._table:
            self._table[state_name] = {}
        self._table[state_name][letter] = transition
        if self._current_state == "": 
            self._current_state = state_name
        

    def delete_state(self, state_name: str) -> None:
        if state_name not in self._table:
            raise ValueError("Состояния с именем {state_name} не найдено")
        self._table.pop(state_name, None)


    def set_state(self, state_name: str) -> None:
        if state_name not in self._table:
            raise ValueError("Состояния с именем {state_name} не найдено")
        self._current_state = state_name


    def clear_table(self) -> None:
        self._table = {}
        self._current_state = ""


    @property
    def table(self):
        return self._table
    

    def get_current_transition(self, letter: str) -> Transition:
        if self._current_state == "":
            raise RuntimeError("Состояние не установлено")
        try:
            return self._table[self._current_state][letter] 
        except KeyError:
            raise RuntimeError(f"Нет перехода для состояния {self._current_state} и символа {letter}")