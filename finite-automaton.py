import logging

class FiniteAutomaton:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.transitions = {}
        self.initial_state = ""
        self.final_states = set()

    def read_input(self, filename):
        with open(filename, 'r') as file:
            self.initial_state = file.readline().strip()
            self.alphabet = set(file.readline().split())
            self.states = set(file.readline().split())
            self.final_states = set(file.readline().split())

            for line in file:
                source, target, symbol = line.split()
                self.transitions.setdefault((source, symbol), []).append(target)

            print(f'Automaton transitions are [{self.transitions}]')
            print(f'Automaton final states are [{self.final_states}]')


    def epsilon_closure(self, states):
        closure = set(states)
        stack = list(states)

        while stack:
            state = stack.pop()
            if (state, '&') in self.transitions:
                for target_state in self.transitions[(state, '&')]:
                    if target_state not in closure:
                        closure.add(target_state)
                        stack.append(target_state)

        return closure

    def run(self, word):
        current_states = self.epsilon_closure([self.initial_state])

        for symbol in word:
            if symbol not in self.alphabet:
                print(f'ERROR -- The given symbol [{symbol}] is not present in automatons alphabet')
                return False

            next_states = set()

            for state in current_states:
                if (state, symbol) in self.transitions:
                    next_states.update(self.transitions[(state, symbol)])

            current_states = self.epsilon_closure(next_states)

        return any(state in self.final_states for state in current_states)


def main():
    automaton = FiniteAutomaton()
    filename = "automaton-1.txt"

    try:
        automaton.read_input(filename)
    except FileNotFoundError:
        print("File not found.")
        return

    word = input("Enter a word: ")
    if automaton.run(word):
        print("Accept")
    else:
        print("Reject")


if __name__ == "__main__":
    main()
