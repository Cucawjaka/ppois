import sys, json

from main import Direction, Transition, TuringMachine, TuringMachineCLI


def load_from_file(path: str) -> TuringMachine:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    tm = TuringMachine()
    tm.set_alphabet(data["alphabet"])
    tm.load_word(data["word"])

    for state_name, states in data["states"].items():
        for letter, state in states.items():
            transition = Transition(
                write=state["write"],
                move=Direction(state["move"]),
                next_state=state["next_state"],
                stop=state["stop"]
            )
            tm.load_state(letter, state_name, transition)

    return tm



if __name__ == "__main__": #pragma: no cover
    import sys
    if len(sys.argv) < 2:
        print("Использование: python3 -m script <path> [-log]")
        sys.exit(1)

    path = sys.argv[1]
    log = "-log" in sys.argv
    tm = load_from_file(path)
    cli = TuringMachineCLI(tm)

    if log:
        print("Нажмите 'n' для следующего шага, 'q' - для выхода\n\n")
        while True:
            user_input = input()
            if user_input == 'n':
                done = cli.print_step()
                cli.output_tape()
        
            if done or user_input == 'q':
                break
    else:
        cli.output_result()