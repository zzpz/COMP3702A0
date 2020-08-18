from unittest import TestCase
from which_state import *

class Test(TestCase):


    def setUp(self) -> None:
        self.inputs = ['12345678_','12345_786','1234_5786','_12345678','1_2345678']


    def test_transition(self):
        for input in self.inputs:
            pass


