from unittest import TestCase
from which_state import *

class Test(TestCase):


    def setUp(self) -> None:
        self.inputs = ['_12345678','12345678_','12345_786','1234_5786','_12345678','1_2345678']




    def test_transition(self):
        for input in self.inputs:
            state = State(input)
            action_states = get_next_states_given_action(state)
            node = Node(state,action_states)
            print(node)


    def test_compare_same(self):
        i = 0
        state1 = State(self.inputs[i])
        state2 = State(self.inputs[i])

        d = compare(state1,state2)
        self.assertTrue('L' in d)
