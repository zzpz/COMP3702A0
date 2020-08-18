from unittest import TestCase
from which_action import *

class Test(TestCase):


    def setUp(self) -> None:
        self.inputs = ['_12345678','12_345678','12345678_','123456_78','12345_786','1234_5786','1_2345678','123_45678','1_2345768']

        ## could be a map of (1,2) : answer


    def test_transition(self):
        for input in self.inputs:
            state = State(input)
            action_states = get_next_states_given_action(state)
            node = Node(state,action_states)
            print(node)


    def test_compare_same_corner_1(self):
        inputs = [0]
        for i in inputs:

            state1 = State(self.inputs[i])
            state2 = State(self.inputs[i])

            d = compare(state1,state2)
            self.assertTrue('L' in d and 'U' in d)


    def test_compare_same_corner_2(self):
        inputs = [1]
        for i in inputs:
            state1 = State(self.inputs[i])
            state2 = State(self.inputs[i])

            d = compare(state1, state2)
            self.assertTrue('R' in d and 'U' in d)

    def test_compare_same_corner_3(self):
        inputs = [2]
        for i in inputs:
            state1 = State(self.inputs[i])
            state2 = State(self.inputs[i])

            d = compare(state1, state2)
            self.assertTrue('R' in d and 'D' in d)

    def test_compare_same_corner_4(self):
        inputs = [3]
        for i in inputs:
            state1 = State(self.inputs[i])
            state2 = State(self.inputs[i])

            d = compare(state1, state2)
            self.assertTrue('L' in d and 'D' in d and 'U' not in d)

    def test_excepts(self):

        for i in range(len(self.inputs)):
            for j in range(len(self.inputs)):
                state1 = State(self.inputs[i])
                state2 = State(self.inputs[j])

                d = compare(state1, state2)

    def test_impossible(self):
        i=0
        j=8
        state1 = State(self.inputs[i])
        state2 = State(self.inputs[j])
        d=compare(state1,state2)

        self.assertEqual(d,[])