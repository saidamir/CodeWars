import unittest

from katas.kyu_7.odd_ladder import pattern


class OddLadderTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(pattern(4), '1\n333')

    def test_equals_2(self):
        self.assertEqual(pattern(1), '1')

    def test_equals_3(self):
        self.assertEqual(pattern(5), '1\n333\n55555')
