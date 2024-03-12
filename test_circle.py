"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import math
import unittest
from circle import Circle


class CircleTest(unittest.TestCase):
    """test of the Circle class"""

    def test_check_radius_and_area(self):
        """Check area and radius of Circle class"""
        self.assertEqual(6, Circle(6).get_radius())
        self.assertEqual(math.pi * 36, Circle(6).get_area())

    def test_typical_case(self):
        """test if add positive radius working or not"""
        self.assertEqual(f"{Circle(math.sqrt(6 ** 2 + 7 ** 2))}", f"{Circle(7).add_area(Circle(6))}")
        self.assertEqual(Circle(math.sqrt(6 ** 2 + 7 ** 2)).get_radius(), Circle(7).add_area(Circle(6)).get_radius())
        self.assertEqual(Circle(math.sqrt(6 ** 2 + 7 ** 2)).get_area(), Circle(7).add_area(Circle(6)).get_area())

        self.assertEqual(f"{Circle(math.sqrt(99 ** 2 + 98 ** 2))}", f"{Circle(98).add_area(Circle(99))}")
        self.assertEqual(Circle(math.sqrt(99 ** 2 + 98 ** 2)).get_radius(),
                         Circle(98).add_area(Circle(99)).get_radius())
        self.assertEqual(Circle(math.sqrt(99 ** 2 + 98 ** 2)).get_area(), Circle(98).add_area(Circle(99)).get_area())

    def test_negative_radius(self):
        """User can't input negative radius"""
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_edge_case(self):
        """test if one Circle has radius 0 and other has non-zero it should be the same"""
        self.assertEqual(f"{Circle(math.sqrt(6 ** 2 + 0 ** 2))}", f"{Circle(6).add_area(Circle(0))}")
        self.assertEqual(Circle(math.sqrt(6 ** 2 + 0 ** 2)).get_radius(), Circle(6).add_area(Circle(0)).get_radius())
        self.assertEqual(Circle(math.sqrt(6 ** 2 + 0 ** 2)).get_area(), Circle(6).add_area(Circle(0)).get_area())

        self.assertEqual(f"{Circle(math.sqrt(44 ** 2 + 0 ** 2))}", f"{Circle(44).add_area(Circle(0))}")
        self.assertEqual(Circle(math.sqrt(44 ** 2 + 0 ** 2)).get_radius(), Circle(44).add_area(Circle(0)).get_radius())
        self.assertEqual(Circle(math.sqrt(44 ** 2 + 0 ** 2)).get_area(), Circle(44).add_area(Circle(0)).get_area())
