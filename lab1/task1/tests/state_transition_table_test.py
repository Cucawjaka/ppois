import pytest


from turing_machine.state_transition_table import StateTransitionTable
from turing_machine.transition import Transition
from task1.tests.fixtures import state_table, transition, state_table_with_transition


def test_add_state(state_table: StateTransitionTable, transition: Transition):
    state_table.add_state(transition, "b", "q0")

    assert "q0" in state_table._table
    assert "b" in state_table._table["q0"]
    assert state_table._current_state == "q0"


def test_delete_state(state_table_with_transition: StateTransitionTable):
    state_table_with_transition.delete_state("q0")
    
    assert "q0" not in state_table_with_transition._table


def test_delete_state_with_exception(state_table: StateTransitionTable):
    with pytest.raises(ValueError):
        state_table.delete_state("qo")


def test_set_state(state_table_with_transition: StateTransitionTable):
    state_table_with_transition.set_state("q0")

    assert state_table_with_transition._current_state == "q0"


def test_set_state_with_exception(state_table: StateTransitionTable):
    with pytest.raises(ValueError):
        state_table.set_state("q0")


def test_clear_table(state_table_with_transition: StateTransitionTable):
    state_table_with_transition.clear_table()

    assert state_table_with_transition._table == {}
    assert state_table_with_transition._current_state == ""


def test_get_current_transition(
        state_table_with_transition: StateTransitionTable,
        transition: Transition):
    returned_transition = state_table_with_transition.get_current_transition("b")

    assert returned_transition == transition


def test_get_current_transition_without_current_state(state_table: StateTransitionTable):
    with pytest.raises(RuntimeError):
        state_table.get_current_transition("a")


def test_get_current_transition_without_letter_state(state_table_with_transition: StateTransitionTable):
    with pytest.raises(RuntimeError):
        state_table_with_transition.get_current_transition("a")