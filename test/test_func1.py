import unittest

from func1.func1 import main_1


class test_func1_main(unittest.TestCase):

    def test_func1(self):
        correct = 'Hello from IL!'
        actual = main_1()
        self.assertEqual(actual, correct)


if __name__ == '__main__':
    unittest.main()
