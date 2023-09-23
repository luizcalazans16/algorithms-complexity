## Universidade La Salle Algorithms complexity

In order to test different automaton definitions, we must change the file name at `line 53`.


### How does the code work?

The most important functions of this code snippet are:

**Read Input (read_input method):**
- Reads the description of the automaton from a file.
- Initializes the automaton's properties like the initial state, alphabet, states, and final states.
- Parses transition lines from the file and populates the transitions dictionary, representing transitions between states based on symbols.

**Epsilon Closure (epsilon_closure method):**
- Computes the epsilon closure of a given set of states. Epsilon closure is the set of states reachable from a state using epsilon (empty) transitions.
- Uses a stack-based approach to iteratively add reachable states to the closure set.
- Includes states reachable through epsilon transitions.

**Run Automaton (run method):**
- Simulates the automaton's behavior on an input word.
- Initializes the current states with the epsilon closure of the initial state.
- Validates if the current character(symbol) in the given word is present in automaton's alphabet definition
- Computes the next set of states by following transitions based on the symbol.
- Applies epsilon closures to include possible epsilon transitions.
- Checks if any resulting state is a final state, indicating whether the word is accepted or not.
