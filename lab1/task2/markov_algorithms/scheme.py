from markov_algorithms.formula import Formula


class Scheme:
    def __init__(self) -> None:
        self._scheme: list[Formula] = list()


    def add_formula(self, formula: Formula) -> None:
        if formula in self._scheme:
            raise ValueError("Формула уже существует")
        self._scheme.append(formula)


    def delete_formula(self, formula_to_delete: Formula) -> None:
        if formula_to_delete in self._scheme:
            self._scheme.remove(formula_to_delete)


    def clear_scheme(self) -> None:
        self._scheme = list()


    @property
    def scheme(self) -> list[Formula]:
        return self._scheme
    

    def get_substituiting_value(self, tape: str) -> Formula | None:
        for formula in self._scheme:
            index = tape.find(formula.old_value)
            if index != -1:
                return formula
        return None