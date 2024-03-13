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

    def test_increment_method(self):
        """test increment method in counter"""
        before_increment = self.counter.count
        self.assertEqual(before_increment + 1, self.counter.increment())
        self.assertEqual(before_increment + 2, self.counter.increment())

    def test_instance(self):
        """check if someone call Counter() again it will be the same one or not"""
        counter = Counter()
        counter2 = Counter()

        self.assertIs(counter, counter2)

        counter2.increment()
        self.assertEqual(counter.count, counter2.count)
        counter.increment()
        self.assertEqual(counter.count, counter2.count)
