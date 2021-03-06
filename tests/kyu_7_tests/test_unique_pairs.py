import unittest

from katas.kyu_7.unique_pairs import projectPartners


class UniquePairsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(projectPartners(2), 1)

    def test_equals_2(self):
        self.assertEqual(projectPartners(3), 3)

    def test_equals_3(self):
        self.assertEqual(projectPartners(4), 6)

    def test_equals_4(self):
        self.assertEqual(projectPartners(5), 10)
