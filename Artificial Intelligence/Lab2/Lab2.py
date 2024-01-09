# Justin Chung Lab2.py
class VacuumCleanerAgent:
    def __init__(self):
        # Initialize actions list to keep track of performed actions.
        self.actions = []

    def goal_test(self, state):
        # Check if both left and right spots are Clean
        if state[0] == "Clean" and state[1] == "Clean":
            return True
        else:
            return False

    def action(self, state):
        # Check if current spot of Vacuum is Dirty
        if state[state[2]] == "Dirty":
            return "Suck"
        # Current spot not dirty and currently on left spot, so move right
        elif state[2] == 0:
            return "Right"
        # Current spot not dirty and currently on right spot, so move left
        else:
            return "Left"

    def update_state(self, state, action):
        # Make copy of state in order to prevent unintended changes and to keep history of states.
        if action == "Suck":
            # Clean the current spot where the Vacuum is located
            state[state[2]] = "Clean"
        elif action == "Left":
            # Move to the left spot
            state[2] = 0
        elif action == "Right":
            # Move to the right spot
            state[2] = 1
        # Add the performed action in the actions list
        self.actions.append(action)
        return state

