import unittest

from katas.beta.divisible_by_four import divisible_by_four


class DivisibleByFourTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(divisible_by_four(12))

    def test_false(self):
        self.assertFalse(divisible_by_four(7))
