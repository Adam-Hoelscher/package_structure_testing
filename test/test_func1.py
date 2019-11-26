import unittest

from func1.func1 import main_1

class test_func1_main(unittest.TestCase):

    def test_func(self):
        correct = 'Hello from IL!'
        actual = main_1()
        self.assertEqual(actual, correct)
