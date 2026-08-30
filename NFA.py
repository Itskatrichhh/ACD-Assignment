# NFA for binary strings containing the substring "01"

states = {"q0", "q1", "q2"}
alphabet = {"0", "1"}

start_state = "q0"
final_states = {"q2"}

# NFA transitions
transitions = {
    ("q0", "0"): {"q0", "q1"},
    ("q0", "1"): {"q0"},
    ("q1", "0"): set(),
    ("q1", "1"): {"q2"},
    ("q2", "0"): {"q2"},
    ("q2", "1"): {"q2"}
}


# Function to simulate the NFA
def simulate_nfa(input_string):
    if any(ch not in alphabet for ch in input_string):
        return "Invalid Input", []

    current_states = {start_state}
    path = [current_states]

    for symbol in input_string:
        next_states = set()

        for state in current_states:
            if (state, symbol) in transitions:
                next_states.update(transitions[(state, symbol)])

        current_states = next_states
        path.append(current_states)

    if current_states & final_states:
        return "Accepted", path
    else:
        return "Rejected", path


# Valid Test - 1
test_string_1 = "1101"
status_1, path_1 = simulate_nfa(test_string_1)

print("Input String:", test_string_1)

for i, states_now in enumerate(path_1):
    if i == 0:
        print("Start:", states_now)
    else:
        print("After reading", test_string_1[i - 1], ":", states_now)

print("Result:", status_1)


# Valid Test - 2
test_string_2 = "111"
status_2, path_2 = simulate_nfa(test_string_2)

print("\nInput String:", test_string_2)

for i, states_now in enumerate(path_2):
    if i == 0:
        print("Start:", states_now)
    else:
        print("After reading", test_string_2[i - 1], ":", states_now)

print("Result:", status_2)


# Invalid Test
test_string_3 = "101a"
status_3, path_3 = simulate_nfa(test_string_3)

print("\nInput String:", test_string_3)
print("Result:", status_3)
