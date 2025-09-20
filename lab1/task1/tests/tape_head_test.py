import pytest


from turing_machine.direction import Direction
from turing_machine.tape_head import EMPTY_SYMBOL, NO_WRITE_SYMBOL, TapeHead
from tests.fixtures import tape_head


@pytest.mark.parametrize(
        "direction, excepted_position, start_position",
        [(Direction.RIGHT, 3, 2),
         (Direction.LEFT, 2, 3),
         (Direction.NONE, 3, 3)]
)
def test_move(
    direction: Direction,
    excepted_position: int,
    start_position: int,
    tape_head: TapeHead,
    ) -> None:
    tape_head.set_word("abcd")
    tape_head._position = start_position

    tape_head.move(direction)

    assert tape_head.position == excepted_position


@pytest.mark.parametrize(
        "direction, position, expected_symbol_index",
        [(Direction.LEFT, 0, 0),
         (Direction.RIGHT, 2, 3)]
)
def test_move_with_moving_outside(direction: Direction,
                                  position: int,
                                  expected_symbol_index: int,
                                  tape_head: TapeHead) -> None:

    tape_head.set_word("a")
    old_len = len(tape_head._tape)

    tape_head._position = position
    tape_head.move(direction)

    assert len(tape_head._tape) == old_len + 1
    assert tape_head._tape[expected_symbol_index] == "_"


@pytest.mark.parametrize(
        "written_value, excepted_value",
        [(NO_WRITE_SYMBOL, None), ("a", "a")]
)
def test_write(written_value: str, excepted_value, tape_head: TapeHead) -> None:
    if not excepted_value: excepted_value = tape_head._tape[tape_head.position]

    tape_head.write(written_value)
    assert tape_head._tape[tape_head.position] == excepted_value


def test_read(tape_head: TapeHead):
    tape_head.set_word("a")

    assert tape_head.read() == "a"


@pytest.mark.parametrize(
        "old_tape, word, excepted_tape",
        [(None, "a", [EMPTY_SYMBOL, "a", EMPTY_SYMBOL]),
         ([EMPTY_SYMBOL, "a", EMPTY_SYMBOL], "a", [EMPTY_SYMBOL, "a", "a", EMPTY_SYMBOL])]
)
def test_set_word(old_tape, word, excepted_tape, tape_head):
    if old_tape: tape_head._tape = old_tape 
    tape_head.set_word(word)

    assert tape_head._tape == excepted_tape


def test_clear(tape_head: TapeHead):
    tape_head.set_word("abc")
    tape_head.clear()

    assert tape_head._tape == [EMPTY_SYMBOL]
    assert tape_head.position == 0