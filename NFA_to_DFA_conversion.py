# NFA to DFA Conversion using Subset Construction

states = {"q0", "q1", "q2"}
alphabet = {"0", "1"}

start_state = "q0"
final_states = {"q2"}

# NFA transition table
nfa_transitions = {
    ("q0", "0"): {"q0", "q1"},
    ("q0", "1"): {"q0"},
    ("q1", "0"): set(),
    ("q1", "1"): {"q2"},
    ("q2", "0"): {"q2"},
    ("q2", "1"): {"q2"}
}


def move(state_set, symbol):
    result = set()

    for state in state_set:
        if (state, symbol) in nfa_transitions:
            result.update(nfa_transitions[(state, symbol)])

    return result

# Convert NFA to DFA
def convert_nfa_to_dfa():

    dfa_states = []
    dfa_transitions = {}

    start = frozenset({start_state})

    dfa_states.append(start)

    index = 0

    while index < len(dfa_states):

        current = dfa_states[index]
        index += 1

        for symbol in alphabet:

            next_state = frozenset(move(current, symbol))

            dfa_transitions[(current, symbol)] = next_state

            if next_state not in dfa_states:
                dfa_states.append(next_state)

    return dfa_states, dfa_transitions


# Convert the NFA
dfa_states, dfa_transitions = convert_nfa_to_dfa()


# Display DFA states
print("DFA States:")

for state in dfa_states:
    print(state)


# Display DFA transitions
print("\nDFA Transitions:")

for state in dfa_states:

    for symbol in alphabet:

        next_state = dfa_transitions[(state, symbol)]

        print(state, "--", symbol, "-->", next_state)


# Find DFA final states
dfa_final_states = []

for state in dfa_states:

    if set(state) & final_states:
        dfa_final_states.append(state)


print("\nDFA Start State:")
print(frozenset({start_state}))


print("\nDFA Final States:")

for state in dfa_final_states:
    print(state)
