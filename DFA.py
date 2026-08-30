# Function to simulate the DFA 
def simulate_dfa(input_string):
    if any(ch not in "01" for ch in input_string):
        return "Invalid Input", []

    current = start_state
    path = [current]

    for symbol in input_string:
        if (current, symbol) in transitions:
            current = transitions[(current, symbol)]
            path.append(current)
        else:
            return "Rejected (No transition found)", path

    accepted = current in final_states
    return "Accepted" if accepted else "Rejected", path

# Valid test - 1
test_string_1 = "1011"
status_1, state_path_1 = simulate_dfa(test_string_1)
print(f"Input String: {test_string_1}")
print(f"State Path: {' -> '.join(state_path_1)}")
print(f"Result: {status_1}")

# Valid Test - 2
test_string_2 = "1010"
status_2, state_path_2 = simulate_dfa(test_string_2)
print(f"\nInput String: {test_string_2}")
print(f"State Path: {' -> '.join(state_path_2)}")
print(f"Result: {status_2}")

# Invalid Character test
test_string_3 = "101a"
status_3, state_path_3 = simulate_dfa(test_string_3)
print(f"\nInput String: {test_string_3}")
print(f"State Path: {' -> '.join(state_path_3)}")
print(f"Result: {status_3}")
