"""
Sample tests for github actions
"""
from django.test import SimpleTestCase
from app import sample_calculations


class SampleCalculationsTests(SimpleTestCase):
    """A simple calculation class"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = sample_calculations.add(2, 3)
        self.assertEqual(res, 5)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = sample_calculations.subtract(4, 3)
        self.assertEqual(res, 1)
