from django.test import TestCase
from app.calc import add, subtract


class CalcTest(TestCase):

    def test_two_numbers(self):
        """Test That 2 numbers are added together"""
        self.assertEqual(add(3, 4), 7)

    def test_subtract_numbers(self):
        """Test that subtract 2 numbers and return"""
        self.assertEqual(subtract(14, 8), 6)
