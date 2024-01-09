# Justin Chung Lab2test.py
from Lab2 import VacuumCleanerAgent
import unittest

# Testing
class TestVacuumCleanerAgent(unittest.TestCase):
    def test_clean_squares_start_left(self):
        # Test case: Both squares are initially clean
        initial_state = ["Clean", "Clean", 0]
        expected_actions = []
        expected_cost = 0
        agent = VacuumCleanerAgent()

        # Check if agent's actions achieve the goal state
        while not agent.goal_test(initial_state):
            next_action = agent.action(initial_state)
            initial_state = agent.update_state(initial_state, next_action)

        # Verify that the agent's actions and cost match the expected values
        self.assertEqual(agent.actions, expected_actions)
        self.assertEqual(len(agent.actions), expected_cost)
        
    def test_clean_squares_start_right(self):
        # Test case: Both squares are initially clean
        initial_state = ["Clean", "Clean", 1]
        expected_actions = []
        expected_cost = 0
        agent = VacuumCleanerAgent()

        # Check if agent's actions achieve the goal state
        while not agent.goal_test(initial_state):
            next_action = agent.action(initial_state)
            initial_state = agent.update_state(initial_state, next_action)

        # Verify that the agent's actions and cost match the expected values
        self.assertEqual(agent.actions, expected_actions)
        self.assertEqual(len(agent.actions), expected_cost)

    def test_left_dirty_square_start_left(self):
        # Test case: Left square is initially dirty
        initial_state = ["Dirty", "Clean", 0]
        expected_actions = ["Suck"]
        expected_cost = 1
        agent = VacuumCleanerAgent()

        # Check if agent's actions achieve the goal state
        while not agent.goal_test(initial_state):
            next_action = agent.action(initial_state)
            initial_state = agent.update_state(initial_state, next_action)

        # Verify that the agent's actions and cost match the expected values
        self.assertEqual(agent.actions, expected_actions)
        self.assertEqual(len(agent.actions), expected_cost)
        
    def test_left_dirty_square_start_right(self):
        # Test case: Left square is initially dirty
        initial_state = ["Dirty", "Clean", 1]
        expected_actions = ["Left", "Suck"]
        expected_cost = 2
        agent = VacuumCleanerAgent()

        # Check if agent's actions achieve the goal state
        while not agent.goal_test(initial_state):
            next_action = agent.action(initial_state)
            initial_state = agent.update_state(initial_state, next_action)

        # Verify that the agent's actions and cost match the expected values
        self.assertEqual(agent.actions, expected_actions)
        self.assertEqual(len(agent.actions), expected_cost)

    def test_right_dirty_square_start_left(self):
        # Test case: Right square is initially dirty, start on left
        initial_state = ["Clean", "Dirty", 0]
        expected_actions = ["Right", "Suck"]
        expected_cost = 2
        agent = VacuumCleanerAgent()

        # Check if agent's actions achieve the goal state
        while not agent.goal_test(initial_state):
            next_action = agent.action(initial_state)
            initial_state = agent.update_state(initial_state, next_action)

        # Verify that the agent's actions and cost match the expected values
        self.assertEqual(agent.actions, expected_actions)
        self.assertEqual(len(agent.actions), expected_cost)
        
    def test_right_dirty_square_start_right(self):
        # Test case: Right square is initially dirty, start on right
        initial_state = ["Clean", "Dirty", 1]
        expected_actions = ["Suck"]
        expected_cost = 1
        agent = VacuumCleanerAgent()

        # Check if agent's actions achieve the goal state
        while not agent.goal_test(initial_state):
            next_action = agent.action(initial_state)
            initial_state = agent.update_state(initial_state, next_action)

        # Verify that the agent's actions and cost match the expected values
        self.assertEqual(agent.actions, expected_actions)
        self.assertEqual(len(agent.actions), expected_cost)

    def test_both_dirty_squares_start_left(self):
        # Test case: Both squares are initially dirty, start on left
        initial_state = ["Dirty", "Dirty", 0]
        expected_actions = ["Suck", "Right", "Suck"]
        expected_cost = 3
        agent = VacuumCleanerAgent()

        # Check if agent's actions achieve the goal state
        while not agent.goal_test(initial_state):
            next_action = agent.action(initial_state)
            initial_state = agent.update_state(initial_state, next_action)

        # Verify that the agent's actions and cost match the expected values
        self.assertEqual(agent.actions, expected_actions)
        self.assertEqual(len(agent.actions), expected_cost)
        
    def test_both_dirty_squares_start_right(self):
        # Test case: Both squares are initially dirty, start on right
        initial_state = ["Dirty", "Dirty", 1]
        expected_actions = ["Suck", "Left", "Suck"]
        expected_cost = 3
        agent = VacuumCleanerAgent()

        # Check if agent's actions achieve the goal state
        while not agent.goal_test(initial_state):
            next_action = agent.action(initial_state)
            initial_state = agent.update_state(initial_state, next_action)

        # Verify that the agent's actions and cost match the expected values
        self.assertEqual(agent.actions, expected_actions)
        self.assertEqual(len(agent.actions), expected_cost)
        
if __name__ == '__main__':
    # Run the tests
    unittest.main()
