"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
from counter import Counter
import unittest


class CounterTest(unittest.TestCase):
    """test of the Counter class"""

    def setUp(self) -> None:
        """Create an auction before each test."""
        self.counter = Counter()

    def test_invoking_count(self):
        """test invoking count doesn't change anything"""
        first_count = self.counter.count
        second_count = self.counter.count
        self.assertEqual(first_count, second_count)

    def test_instance(self):
        """check test case in github"""

        counter = Counter()
        self.assertEqual(0, counter.count)
        self.assertEqual(0, counter.count)  # invoking count doesn't change anything

        self.assertEqual(1, counter.increment())  # add 1 and return the new count

        counter2 = Counter()
        self.assertIs(counter, counter2)
        self.assertEqual(1, counter2.count)  # shares same count

        self.assertEqual(2, counter2.increment())  # add 1 and return the new count
        self.assertEqual(2, counter.count)
